from .import views
from django.contrib import admin
from django.urls  import path , include

from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

admin.site.site_header = "WJBB Administration"
admin.site.site_title = "WJBB Administration"

urlpatterns = [
    
    path('', views.index , name = 'index'),
    
    path('pagenotfound', views.pagenotfound, name = 'pagenotfound'), 

    path('contact', views.contact, name = 'contact'),

    path('archives', views.archives, name = 'archives'),

    path('resources_authors', views.resources_authors, name = 'resources_authors'),
    path('resources_reviews', views.resources_reviews, name = 'resources_reviews'),
    path('resources_editors', views.resources_editors, name = 'resources_editors'),
    path('resources_policy', views.resources_policy, name = 'resources_policy'),

    path('about', views.about, name = 'about'),
    path('mission', views.mission, name = 'mission'),
    path('vision', views.vision, name = 'vision'),
    path('editor_board', views.editor_board, name = 'editor_board'),  
    path('article_processing_charges', views.article_processing_charges, name = 'article_processing_charges'), 
    path('team', views.team, name = 'team'),
    path('author_guidelines', views.author_guidelines, name = 'author_guidelines'),
    path('editorial_workflow', views.editorial_workflow, name = 'editorial_workflow'),        
    path('feedback', views.feedback, name = 'feedback'),
    path('our_policies', views.our_policies, name = 'our_policies'),
    path('terms_and_conditions', views.terms_and_conditions, name = 'terms_and_conditions'),
    path('privacy_policy', views.privacy_policy, name = 'privacy_policy'),

    path('join_us', views.join_us, name = 'join_us'),
    path('editor_join_us', views.editor_join_us, name = 'editor_join_us'),
    path('review_join_us', views.review_join_us, name = 'review_join_us'),

    path('submit', views.submit, name = 'submit'),

    path('submitted_artical', views.submitted_artical, name = 'submitted_artical'),
    path('review_paper/<str:paper_id>/', views.submitted_artical_detail, name = 'submitted_artical_detail'),
    
########################----------Payment GetWay ----------########################

    path('subscription', views.subscription, name = 'subscription'), 

    path('payment', views.payment.as_view(), name = 'payment'),
    path('payment_ultimate', views.payment_ultimate.as_view(), name = 'payment_ultimate'),

    path('payment_success', views.payment_success, name = 'payment_success'), 
    path('payment_success_ultimate', views.payment_success_ultimate, name = 'payment_success_ultimate'), 
    

########################----------Payment GetWay ----------########################

    path('login_register', views.login_register, name = 'login_register'), 

    path('login', views.handlelogin, name = 'handlelogin'), 
    path('logout', views.handlelogout, name = 'handlelogout'),

    path('search', views.search, name = 'search'),

    path('profile', views.profile, name = 'profile'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)