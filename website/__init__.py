from flask import Flask, render_template
# from .routes.chatbot import chatbot  # Temporarily disabled chatbot

def create_app():
    app = Flask(__name__)

    # Import other blueprints
    from .routes.home import home
    from .routes.home_intro import home_intro
    from .routes.home_visionmission import home_visionmission
    from .routes.home_keystats import home_keystats
    from .routes.home_services import home_services
    from .routes.home_about import home_about
    from .routes.home_why import home_why
    from .routes.home_testimonials import home_testimonials
    from .routes.home_ourclients import home_ourclients
    from .routes.home_industry import home_industry
    from .routes.home_affiliations import home_affiliations
    from .routes.home_techstack import home_techstack
    from .routes.home_contactus import home_contactus
    from .routes.contact import contact

    from .routes.aboutus import aboutus
    from .routes.aboutus_ourfounder import aboutus_ourfounder
    from .routes.aboutus_ourteam import aboutus_ourteam
    from .routes.aboutus_awardsrecognitions import aboutus_awardsrecognitions
    from .routes.aboutus_milestones import aboutus_milestones
    from .routes.aboutus_certifications import aboutus_certifications
    from .routes.aboutus_gallery import aboutus_gallery
    from .routes.aboutus_videos import aboutus_videos
    
    from .routes.usefulsites import usefulsites
    from .routes.latestnews import latestnews
    from .routes.bulletin import bulletin

    from .routes.joinus import joinus
    from .routes.joinusform import joinusform 
    
    from .routes.privacy import privacy
    from .routes.termsandconditions import termsandconditions
    from .routes.disclaimer import disclaimer
    from .routes.faq import faq

    # Register all blueprints
    app.register_blueprint(home)
    app.register_blueprint(home_intro)
    app.register_blueprint(home_visionmission)
    app.register_blueprint(home_keystats)
    app.register_blueprint(home_services)
    app.register_blueprint(home_about)
    app.register_blueprint(home_why)
    app.register_blueprint(home_testimonials)
    app.register_blueprint(home_ourclients)
    app.register_blueprint(home_industry)
    app.register_blueprint(home_affiliations)
    app.register_blueprint(home_techstack)
    app.register_blueprint(home_contactus)
    app.register_blueprint(contact)

    app.register_blueprint(aboutus)
    app.register_blueprint(aboutus_ourfounder)
    app.register_blueprint(aboutus_ourteam)
    app.register_blueprint(aboutus_awardsrecognitions)
    app.register_blueprint(aboutus_milestones)
    app.register_blueprint(aboutus_certifications)
    app.register_blueprint(aboutus_gallery)
    app.register_blueprint(aboutus_videos)
    
    app.register_blueprint(usefulsites)
    app.register_blueprint(latestnews)
    app.register_blueprint(bulletin)
    
    app.register_blueprint(joinus)
    app.register_blueprint(joinusform)

    app.register_blueprint(privacy)
    app.register_blueprint(termsandconditions)
    app.register_blueprint(disclaimer)
    app.register_blueprint(faq) 

   # Register chatbot blueprint
    from .routes.chatbot import chatbot
    app.register_blueprint(chatbot, url_prefix='/chatbot')

    # Optional route to serve the chatbot interface HTML
    @app.route('/chatbot')
    def serve_chatbot():
        return render_template('chatbot.html')

    app.secret_key = 'a-very-long-random-secret-key-1234567890abcdef'
    return app
