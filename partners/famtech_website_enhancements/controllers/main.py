from odoo import http
from odoo.http import request

class FamtechWebsite(http.Controller):
    
    @http.route('/news', type='http', auth="public", website=True)
    def partner_news_page(self, **kw):
        # FETCH THE DATA: Get the most recent published event
        latest_event = request.env['event.event'].sudo().search(
            [('is_published', '=', True)], 
            order='date_begin desc', 
            limit=1
        )
        
        # SEND TO FRONTEND: Pass the fetched data to your XML template
        return request.render("famtech_website_enhancements.news_page_template", {
            'latest_event': latest_event,
        })