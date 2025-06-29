from flask import Blueprint, render_template
import datetime

bulletin = Blueprint('bulletin', __name__)

items = [
    {
        'title': 'GST Return Filing Due Date Extended',
        'summary': 'Government extended GST return filing date for May by 15 days to reduce compliance pressure.',
        'link': 'https://www.cbic.gov.in',
        'date': datetime.date(2025, 5, 22)
    },
    {
        'title': 'New ITR Forms Released for AY 2025-26',
        'summary': 'Income Tax Department rolled out simplified ITR forms to enhance user experience.',
        'link': 'https://www.incometaxindia.gov.in',
        'date': datetime.date(2025, 5, 20)
    },
    {
        'title': 'SEBI’s New Guidelines on IPO Allotment',
        'summary': 'SEBI issued rules for transparent IPO allotment to safeguard retail investors.',
        'link': 'https://www.sebi.gov.in',
        'date': datetime.date(2025, 5, 18)
    },
    {
        'title': 'RBI Cuts Repo Rate by 25 Basis Points',
        'summary': 'The Reserve Bank of India reduced the repo rate to boost economic growth amid slowing inflation.',
        'link': 'https://www.rbi.org.in',
        'date': datetime.date(2025, 5, 15)
    },
    {
        'title': 'NPCI Announces UPI Transaction Cap Changes',
        'summary': 'New transaction caps have been introduced to balance system load across banks.',
        'link': 'https://www.npci.org.in',
        'date': datetime.date(2025, 5, 14)
    },
    {
        'title': 'Income Tax Refunds Now Processed Within 7 Days',
        'summary': 'CBDT ensures faster refunds with upgraded processing systems.',
        'link': 'https://www.incometaxindiaefiling.gov.in',
        'date': datetime.date(2025, 5, 12)
    },
    {
        'title': 'PM Jan Dhan Yojana: Over 50 Crore Accounts Opened',
        'summary': 'The financial inclusion scheme reaches a major milestone across India.',
        'link': 'https://pmjdy.gov.in',
        'date': datetime.date(2025, 5, 10)
    },
    {
        'title': 'New TDS Rules for Freelancers and Gig Workers',
        'summary': 'Income from digital platforms will now be subject to revised TDS slabs.',
        'link': 'https://www.incometax.gov.in',
        'date': datetime.date(2025, 5, 8)
    },
    {
        'title': 'Mutual Funds See Record Inflows in April',
        'summary': 'Retail investors continue to flock to SIPs and equity funds amid bullish market.',
        'link': 'https://www.amfiindia.com',
        'date': datetime.date(2025, 5, 5)
    },
    {
        'title': 'Digital Rupee Pilot Expands to Retail Transactions',
        'summary': 'RBI rolls out digital rupee (e₹) use cases at more merchant and retail outlets.',
        'link': 'https://www.rbi.org.in',
        'date': datetime.date(2025, 5, 2)
    }
]

@bulletin.route('/bulletin')
def show_bulletin():
    return render_template('bulletin.html', news=items)


