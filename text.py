import copy

top_titles = {
    'index': 'Home',
    'github': 'GitHub',
    'milestones': 'Milestones(Open)',
    'milestones-completed': 'Milestones(Completed)'
}

page_titles = {
    'index': 'Open Data Services Dashboard',
    'github': 'GitHub Overview',
    'milestones' : 'GitHub Milestones',
    'milestones-completed' : 'GitHub Milestones (Completed)',

}

page_leads = {
    'index': '',
    'github': 'What are the Open Data Services team doing in GitHub?',
    'milestones': 'What is planned by the Open Data Services team in GitHub?',
    'milestones-completed': 'What has been done by the Open Data Services team in GitHub?',

}
page_sub_leads = {
    'github': 'Overview numbers from the <a href="https://github.com/OpenDataServices">Open Data Services GitHub organisation</a>. GitHub is an online repository used by open-source developers to help them manage their work. The Open Data Services team use it for a variety of reasons, including logging issues in software and guidance.',
    'milestones': 'Calendar of the due dates of all open milestones in every repository belonging to the <a href="https://github.com/OpenDataServices">Open Data Services organisation on GitHub</a>.',
    'milestones-completed': 'Calendar of all CLOSED milestones in every repository belonging to the <a href="https://github.com/OpenDataServicesI">Open Data Services organisation on GitHub</a>.',
}

short_page_titles = copy.copy(page_titles)
short_page_titles.update({
    'github': 'Overview',
    'milestones' : 'Milestones',
    'milestones-completed' : 'Completed Milestones',
})

top_navigation = [
                  #'headlines', 
                  #'data_quality', 
                  #'exploring_data', 
                  'github', 
                  'milestones',
                  'milestones-completed',
                  #'publishing_stats', 
                  #'faq'
                  ]
navigation = {
    #'headlines': [ 'publishers', 'files', 'activities'],
    #'data_quality': ['download', 'xml', 'validation', 'versions', 'licenses', 'organisation', 'identifiers', 'reporting_orgs'],
    #'exploring_data': ['elements', 'codelists', 'booleans', 'dates'],
    #'publishing_stats': ['timeliness', 'forwardlooking']#, 'comprehensiveness'] #, 'coverage' ]
}
