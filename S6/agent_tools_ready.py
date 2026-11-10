"""Working versions of the five Session 6 tools. Load with: from agent_tools_ready import *"""
import json, urllib.request, urllib.parse

def _get(url):
    """Download a URL and read it as JSON (used by the tools below)."""
    with urllib.request.urlopen(url, timeout=20) as r:
        return json.loads(r.read())


def search_trials(condition, location=""):
    """Recruiting trials on ClinicalTrials.gov: one line per trial, 'NCT...: title (phase)'."""
    q = {"query.cond": condition, "filter.overallStatus": "RECRUITING", "pageSize": 5}
    if location:
        q["query.locn"] = location
    studies = _get("https://clinicaltrials.gov/api/v2/studies?" + urllib.parse.urlencode(q)).get("studies", [])
    if not studies:
        return "No recruiting trials found."
    lines = []
    for s in studies:
        p = s["protocolSection"]
        phases = ", ".join(p.get("designModule", {}).get("phases", [])) or "n/a"
        lines.append(f'{p["identificationModule"]["nctId"]}: {p["identificationModule"]["briefTitle"]} ({phases})')
    return "\n".join(lines)


def get_trial(nct_id):
    """One trial's age limits, sex, contact and eligibility criteria, as labelled lines of text."""
    p = _get(f"https://clinicaltrials.gov/api/v2/studies/{nct_id}")["protocolSection"]
    e = p.get("eligibilityModule", {})
    contacts = p.get("contactsLocationsModule", {}).get("centralContacts", [])
    contact = f'{contacts[0].get("name", "?")} <{contacts[0].get("email", "no e-mail listed")}>' if contacts else "none listed"
    return (f'{nct_id}: {p["identificationModule"]["briefTitle"]}\n'
            f'Minimum age: {e.get("minimumAge", "N/A")}\nMaximum age: {e.get("maximumAge", "N/A")}\nSex: {e.get("sex", "ALL")}\n'
            f'Contact: {contact}\nEligibility:\n{e.get("eligibilityCriteria", "")[:1200]}')


def check_age(patient_age, minimum_age, maximum_age):
    """'eligible', 'too young' or 'too old'. Limits are text like '18 Years' or 'N/A'."""
    def years(text):
        if not text or str(text).upper() == "N/A":
            return None
        number = float(str(text).split()[0])
        return number / 12 if "month" in str(text).lower() else number
    low, high = years(minimum_age), years(maximum_age)
    if low is not None and float(patient_age) < low:
        return "too young"
    if high is not None and float(patient_age) > high:
        return "too old"
    return "eligible"


def search_pubmed(query):
    """3 relevant PubMed papers: one line each, 'PMID ...: title (journal, year)'."""
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    ids = _get(base + "esearch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "term": query, "retmode": "json", "retmax": 3, "sort": "relevance"}))["esearchresult"]["idlist"]
    if not ids:
        return "No papers found."
    summ = _get(base + "esummary.fcgi?" + urllib.parse.urlencode({"db": "pubmed", "id": ",".join(ids), "retmode": "json"}))["result"]
    return "\n".join(f'PMID {i}: {summ[i]["title"]} ({summ[i].get("source", "")}, {summ[i].get("pubdate", "")[:4]})' for i in ids)


def send_email(to, subject, text):
    """Simulated: append the e-mail to outbox.txt (never really send). Return a confirmation."""
    with open("outbox.txt", "a", encoding="utf-8") as f:
        f.write(f"TO: {to}\nSUBJECT: {subject}\n{text}\n{'=' * 60}\n")
    return f"E-mail to {to} written to outbox.txt."
