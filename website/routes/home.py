from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/')
def homepage():
    
    services = [
        {"title": "CA", "description": "Our qualified and skilled chartered accountants ensure that your business operations run more efficiently.", "image": "ca.jpg"},
        {"title": "Audit & Assurance", "description": "We undertake internal audits for corporations with the object of bringing in efficiency in the functioning.", "image": "audit.jpg"},
        {"title": "Taxation", "description": "We assist you in making correct and timely tax payments of dues such as advance tax, self assessment tax, etc.", "image": "taxation.jpg"},
        {"title": "Financial Advisory", "description": "We focus on advising the clients in raising of resources through various financial institutions, banks, etc.", "image": "corporate.jpg"},
        {"title": "GST Services", "description": "We are one of the reliable and widely acclaimed service providers of GST consultancy services for registration and refund.", "image": "gst.jpg"}
    ]

    aboutus = {"title": "About Us", "description": "Manish Saraogi & Associates is a professionally managed Chartered Accountancy firm led by CA Manish Saraogi. With a strong commitment to accuracy, integrity, and client service, we offer tailored financial, tax, and advisory solutions to individuals, professionals, startups, and businesses across various sectors. Our core strength lies in combining deep domain expertise with practical insights, enabling our clients to make informed financial decisions and stay compliant in an ever-evolving regulatory environment. From income tax and GST to auditing, company incorporation, and business consultancy, we provide end-to-end support to help our clients achieve clarity, efficiency, and sustainable growth. Over the years, we have built long-standing relationships based on trust, transparency, and consistent performance. Whether you're seeking routine compliance or strategic financial guidance, we strive to be more than just service providers—we aim to be your trusted partners in progress. At Manish Saraogi & Associates, we don’t just manage numbers—we help build futures.", "image": "aboutus.jpg"}
    
    why_us = [
        {"title": "icon 1", "description": "We offer support services that can free up management to concentrate on important aspects of their business.", "image": "whyusicon1.jpg"},
        {"title": "icon 2", "description": "We have proven experience of managing end to end finance and accounts processes from initial invoicing till payment.", "image": "whyusicon2.jpg"},
        {"title": "icon 3", "description": "We turn numbers into actionable business intelligence - building a better picture offering better finance.",  "image": "whyusicon3.jpg"},
        {"title": "icon 4", "description": "We explore ideas and help you plan for a more profitable future wherever you are in your business lifecycle.",  "image": "whyusicon4.jpg"}
    ]

    return render_template('home.html', services=services, aboutus=aboutus, why_us=why_us)
