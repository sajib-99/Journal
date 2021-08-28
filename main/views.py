from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserProfileForm

from .models import Contact
from .models import Editor_Request
from .models import Reviewer_Request
from .models import Submitted_Paper
from articles.models import Post

from django.core.files.storage import FileSystemStorage

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from django.views.generic.base import TemplateView
from django.urls import reverse
import stripe 

stripe.api_key = settings.STRIPE_SECRET_KEY

#index
def index(request):
    allPosts= Post.objects.all().order_by('-timeStamp')

    paginator = Paginator(allPosts, 5)   
    page_num = request.GET.get('page',1)
    page = paginator.page(page_num)

    context={'allPost': page}
    return render(request, 'index.html', context)

#Contact   
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        tropic=request.POST['tropic']
        content =request.POST['content']
        

        if len(name)<2 or len(email)<5 or len(phone)<9 or len(tropic)<5 or len(content)<10:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, tropic=tropic, content=content)
            
            #Send Emial Start
            emailtemplate= render_to_string('email_template.html', {'name':request.POST['name']})

            send_email = EmailMessage(
                'Greetings From WJBB', #Subject
                emailtemplate, #Email_Content
                settings.EMAIL_HOST_USER, #From email
                ['', email], # To Email
                ) 
            fail_silently=False
            send_email.send()
            #Send Emial End

            contact.save()
            messages.success(request, "Your message has been successfully sent")

    return render(request, 'contact.html')

#Join_us
def join_us(request):
    return render(request, 'join-with-us.html')

#Join_us
def editor_join_us(request):

    if request.method=="POST":
            first_name=request.POST['e_first_name']
            last_name=request.POST['e_last_name']
            affiliation=request.POST['e_affiliation']
            email=request.POST['e_email']
            phone=request.POST['e_phone']
            address=request.POST['e_address']
            cv=request.FILES['e_cv']

            if len(first_name)<2 or len(last_name)<2 or len(email)<5 or len(phone)<9 or len(address)<5 :
                messages.error(request, "Please fill the form correctly")
            else:
                editor_request=Editor_Request(First_Name=first_name, Last_Name=last_name, email=email, phone=phone, address=address, affiliation=affiliation, cv=cv)
                
                #Send Emial Start
                emailtemplate= render_to_string('editor_email_template.html', {'name':request.POST['e_first_name']})

                send_email = EmailMessage(
                    'Greetings From WJBB', #Subject
                    emailtemplate, #Email_Content
                    settings.EMAIL_HOST_USER, #From email
                    ['', email], # To Email
                    ) 
                fail_silently=False
                send_email.send()
                #Send Emial End

                editor_request.save()
                messages.success(request, "Your request to Join as the Editorial Board Member successfully sent. Our team will evaluate your profile and get back to you soon")

    return render(request, 'join-with-us.html')

#Join_us
def review_join_us(request):

    if request.method=="POST":
            first_name=request.POST['r_first_name']
            last_name=request.POST['r_last_name']
            affiliation=request.POST['r_affiliation']
            email=request.POST['r_email']
            phone=request.POST['r_phone']
            address=request.POST['r_address']
            cv=request.FILES['r_cv']

            if len(first_name)<2 or len(last_name)<2 or len(email)<5 or len(phone)<9 or len(address)<5 :
                messages.error(request, "Please fill the form correctly")
            else:
                reviewer_request=Reviewer_Request(First_Name=first_name, Last_Name=last_name, email=email, phone=phone, address=address, affiliation=affiliation, cv=cv)
                
                #Send Emial Start
                emailtemplate= render_to_string('review_email_template.html', {'name':request.POST['r_first_name']})

                send_email = EmailMessage(
                    'Greetings From WJBB', #Subject
                    emailtemplate, #Email_Content
                    settings.EMAIL_HOST_USER, #From email
                    ['', email], # To Email
                    ) 
                fail_silently=False
                send_email.send()
                #Send Emial End

                reviewer_request.save()
                messages.success(request, "Your request to Join as the Reviewer successfully sent. Our team will evaluate your profile and get back to you soon")

    return render(request, 'join-with-us.html')


#Archives
def archives(request):
    return render(request, 'archives.html')


#Resources    
def resources_authors(request):
    return render(request, 'resources.html')
def resources_reviews(request):
    return render(request, 'resources2.html')
def resources_editors(request):
    return render(request, 'resources3.html')
def resources_policy(request):
    return render(request, 'resources4.html') 

#About
def about(request):
    return render(request, 'about.html')
def mission(request):
    return render(request, 'mission.html')     
def vision(request):
    return render(request, 'vision.html')
def editor_board(request):
    return render(request, 'editorial-board.html')
def article_processing_charges(request):
    return render(request, 'article-processing-charges.html')
def team(request):
    return render(request, 'team.html')
def author_guidelines(request):
    return render(request, 'author-guidelines.html') 
def editorial_workflow(request):
    return render(request, 'editorial-workflow.html')
def feedback(request):
    return render(request, 'feedback.html') 
def our_policies(request):
    return render(request, 'our-policies.html') 
def terms_and_conditions(request):
    return render(request, 'terms-and-conditions.html')  
def privacy_policy(request):
    return render(request, 'privacy-policy.html') 

#Submit_Articles
def submit(request):

    if request.method=="POST":
            
            author = request.POST['author']
            email = request.POST['email']
            phoneNo = request.POST['phoneNo']
            Country = request.POST['Country']
            address = request.POST['address']
            Article_Title = request.POST['Article_Title']
            Paper_Type = request.POST['Paper_Type']
            Subject_and_Category = request.POST['Subject_and_Category']
            Abstract = request.POST['Abstract']
            paper = request.FILES['paper']

            if len(author)<2 or len(address)<2 or len(email)<5 or len(phoneNo)<7 or len(Article_Title)<5 or len(Paper_Type)<5 or len(Subject_and_Category)<2 or len(Abstract)<50 :
                messages.error(request, "Please fill the form correctly")
            else:
                submitted_paper=Submitted_Paper(author=author, email=email, phoneNo=phoneNo, Country=Country, address=address, Article_Title=Article_Title, Paper_Type=Paper_Type, Subject_and_Category=Subject_and_Category, Abstract=Abstract, paper=paper)
                
                
                #Send Emial Start
                emailtemplate= render_to_string('submit_articles_email_tem.html', {'name':request.POST['author'], 'title':request.POST['Article_Title'] })

                send_email = EmailMessage(
                    'WJBB-Paper Submitted', #Subject
                    emailtemplate, #Email_Content
                    settings.EMAIL_HOST_USER, #From email
                    ['', email], # To Email
                    ) 
                fail_silently=False
                send_email.send()
                #Send Emial End

                submitted_paper.save()
                messages.success(request, "Your article is submitted for review. Please check your email for additional information.")

    return render(request, 'submit.html')

#Submitted Artical Page
def submitted_artical(request):
    allPosts= Submitted_Paper.objects.all().order_by('-id')

    paginator = Paginator(allPosts, 3)   
    page_num = request.GET.get('page',1)
    page = paginator.page(page_num)
    
    context={'items': page}
    
    return render(request,'submitted_paper.html', context)

#Submitted Artical Detail View
def submitted_artical_detail(request, paper_id): 
    post=Submitted_Paper.objects.filter(paper_id=paper_id).first()
    context={"post":post}
    return render(request,'submitted_artical_detail.html',  context)




#Subscription
def subscription(request):
    return render(request, 'subscription.html')


#Payment
class payment(TemplateView):
    template_name = 'payment.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

#PaymentSuccess
def payment_success(request):
        if request.method == 'POST':
            payment_success = stripe.Charge.create(
                amount=60000,
                currency='usd',
                description='WJBB Journal Premium Subscription',
                source=request.POST['stripeToken']
            )
            return render(request, 'payment_success.html')

        return render(request, '404.html')



#Payment
class payment_ultimate(TemplateView):
    template_name = 'payment_ultimate.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

#PaymentSuccess
def payment_success_ultimate(request):
        if request.method == 'POST':
            payment_success = stripe.Charge.create(
                amount=80000,
                currency='usd',
                description='WJBB Journal Ultimate Subscription',
                source=request.POST['stripeToken']
            )
            return render(request, 'payment_success.html')

        return render(request, '404.html')


        
   
#Search
def search(request):
    search=request.GET['search']
    
    if len(search)>50:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=search)
        allPostsAuthor= Post.objects.filter(author__icontains=search)
        allPostsContent =Post.objects.filter(content__icontains=search)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)

    params={'allPosts': allPosts, 'search':search }
    return render(request, 'search.html', params)   



#Login_register  
def login_register(request):
    if  request.method == 'POST':
        form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and  profile_form.is_valid():
            user = form.save()
            
            profile= profile_form.save(commit=False) 
            profile.user = user
            profile.save()           

            #Send Emial Start
            emailtemplate= render_to_string('register_email_template.html', {'name':form.cleaned_data['username'], 'password':form.cleaned_data['password1'] })

            email= form.data.get("Email")

            send_email = EmailMessage(
                'WJBB- Account Created', #Subject
                emailtemplate, #Email_Content
                settings.EMAIL_HOST_USER, #From email
                ['', email], # To Email
                ) 
            fail_silently=False
            send_email.send()
            #Send Emial End
            
            messages.success(request, "Your account has been created successfully. Please check your email for more information")
            return render(request, 'index.html')
        else:
            messages.error(request, "Something went wrong please fill up the form correctly")
            contex = {'form': form, 'profile_form': profile_form}
            return render(request, 'login-register.html', contex)

    else:
        form = UserCreationForm()
        profile_form = UserProfileForm()

    contex = {'form': form, 'profile_form': profile_form}
    return render(request, 'login-register.html', contex) 


#Login
def handlelogin(request):
    if request.method=="POST":
            loginusernmae=request.POST['loginusernmae']
            loginpass=request.POST['loginpass']

            user = authenticate(username=loginusernmae, password=loginpass)

            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In")
                return render(request, 'subscription.html')
            else:
                messages.error(request, "Invalid User Credentials, Please try again.")
                form = UserCreationForm()
                profile_form = UserProfileForm()
                contex = {'form': form, 'profile_form': profile_form}
                return render(request, 'login-register.html', contex) 

    return render(request, '404.html')

#Logout
def handlelogout(request):

    logout(request)
    messages.success(request, "You are logged out from your account")

    form = UserCreationForm()
    profile_form = UserProfileForm()
    contex = {'form': form, 'profile_form': profile_form}
    return render(request, 'login-register.html', contex)

#Profile
def profile(request):
    
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        form = UserCreationForm()
        profile_form = UserProfileForm()
        contex = {'form': form, 'profile_form': profile_form}
        return render(request, 'login-register.html', contex)

 
#404
def pagenotfound(request):
    return render(request, '404.html')
  
