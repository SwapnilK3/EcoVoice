from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import CustomCharityUser,Donation,Event,Blog,Profile
from .utils import * 
import uuid
from django.contrib import messages

#Login signup and logout is remaining

# Create your views here.


def user_login(request) :
    if request.method == 'POST':

        email= request.POST.get('email')
        password= request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # messages.success(request, ("Successfully Login") )
            return redirect('home')
        else:
            return HttpResponse('Unsuccessfully Login') 
             

    return render(request,'Charity/login.html')


@login_required(login_url='login')
def user_logout(request) :
    logout(request)
    # messages.success(request, ("Successfully Logout") )
    return redirect('home')

@login_required(login_url='login')
def home(request):
    
    return render(request,'Charity/charity_home.html')
    
@login_required(login_url='login')
def display_complaint(request):
    if request.method == 'POST':
        # data to delete from the database
        print('successfuly completed complint or discard ')
    
    # Here Show the all compliant 

    return render(request,'complaint_form.html')



def signup(request):
    if request.method == 'POST':
        # Extract data from the request
        email = request.POST.get('email')
        password = request.POST.get('password')
        con_password= request.POST.get('password2')
        
        if(password != con_password):
            messages.success(request, ("Password is not same") )
            return render(request,'Charity/signup.html')
        
        # Create and save the CustomCharityUser object
        
        if AuthUser.objects.filter(username=email).exists():
            messages.success(request, ("User is Already Exist") )
            return redirect('/signup')
        else:
            charity_user=AuthUser.objects.create_user(username=email,password=password)
            
            p_obj = Profile.objects.create(
                user=charity_user,
                email_token = str(uuid.uuid4())
                                        
            )
            send_email_token(email, p_obj.email_token)
             
            CustomCharityUser.objects.create(
                user =charity_user           
            )
       
            return HttpResponse('Verification is send successfully!')
        
    else:
        return render(request,'Charity/signup.html')



def verify(request, token):

    # try:
        obj = Profile.objects.filter(email_token=token).first()
       
        if obj:
            obj.is_verified = True
            obj.save()
            return redirect('login')
        else :
            return HttpResponse('invalid!')

    # except Exception as e:
    #     return HttpResponse('The link is invalid or broken!')

@login_required(login_url='login')
def edit_info(request):
    if request.method == 'POST':
        # Extract data from the request
        
        charity_name = request.POST.get('charity_name')
        charity_id = request.POST.get('charity_id')
        charity_address = request.POST.get('charity_address')
        charity_city = request.POST.get('charity_city')
        charity_country = request.POST.get('charity_country')
        charity_state = request.POST.get('charity_state')
        charity_zipcode = request.POST.get('charity_zipcode')
        

        # Create and save the CustomCharityUser object
        
        CustomCharityUser.objects.filter(user=request.user).update(
            user =request.user,
            charity_name=charity_name,
            charity_id=charity_id,
            charity_country = charity_country,
            charity_address=charity_address,
            charity_city=charity_city,
            charity_state=charity_state,
            charity_zipcode=charity_zipcode
        )
        return render(request,'Charity/succsses.html')

    # return render(request,'edit_info.html', {details:'details'})
    
    return render(request,'Charity/edit_info.html')
    # return HttpResponse('Charity user info edited successfully!') 
    


@login_required(login_url='login')
def about(request):
    
    return render(request,'Charity/about.html')
    # return HttpResponse('here is about page')

@login_required(login_url='login')
def blogs(request):
    
    return render(request,'Charity/blogs.html')


@login_required(login_url='login')
def write_blog(request):
    if request.method == 'POST':
        # Extract data from the request
        author_name = request.POST.get('author_name')
        blog_heading = request.POST.get('blog_heading')
        blog_description = request.POST.get('blog_description')
        uploaded_date = request.POST.get('uploaded_date')

        # Create and save the Blog object
        blog = Blog.objects.create(
            author_name=author_name,
            blog_heading=blog_heading,
            blog_description=blog_description,
            uploaded_date=uploaded_date
        )
        return render(request,'Charity/succsses.html')
 
    return render(request,'Charity/write_blog.html')
    


@login_required(login_url='login')
def event_registration(request):
    if request.method == 'POST':
        # # Extract data from the request
        # event_headline = request.POST.get('event_headline')
        
        # event_address = request.POST.get('event_address')
        # event_city = request.POST.get('event_city')
        # event_country = request.POST.get('event_country')
        # event_state = request.POST.get('event_state')
        # event_date = request.POST.get('event_date')
        # event_zipcode = request.POST.get('event_zipcode')
        
        # # Create and save the Event object
        # event = Event.objects.create(
        #     event_headline=event_headline,
        #     event_host =  CustomCharityUser.objects.filter(user=AuthUser).get("charity_name"),        
        #     event_country=event_country,
        #     event_address=event_address,
        #     event_city=event_city,
        #     event_state=event_state,
            
        #     event_date=event_date
        # )
        # return HttpResponse('Event created successfully!')
        
        return render(request,'Charity/Event_Success.html')
 
    return render(request,'Charity/event_registration.html')
        




# def upcoming_events(request): #it will include in event view
#     return render(request,'upcoming_events.html')

@login_required(login_url='login')
def news(request):
    if request.method == 'POST': # with Condition decorator
        #whenever a user is logged in then it can edit the blog
        print('blog editing')
        
    return render(request,'Charity/news.html')
    


@login_required(login_url='login')
def help(request):
    #it provide some of questions and answer 
    # return render(request,'help.html')
    return HttpResponse('help page')


@login_required(login_url='login')
def donation_details(request):
    if request.method == 'GET':
        # Get the logged-in user's charity name
        if request.user.is_authenticated:
            charity_user = CustomCharityUser.objects.get(email=request.user.email)
            charity_name = charity_user.charity_name
        else:
            return HttpResponse('User not logged in')

        # Filter donations where charity name and beneficiary name are the same
        donations = Donation.objects.filter(beneficiary=charity_name)

        # Pass the filtered data to the HTML template
        return render(request, 'donation_details.html', {'donations': donations})
    else:
        return HttpResponse('Invalid request method')






#Condition decorator: I see. If you want to apply the login_required 
# decorator only to the post requests, but not to the get requests,
# you can use a conditional decorator. A conditional decorator is a function 
# that takes a view function and a condition as arguments, and returns either 
# the original view function or the decorated view function based on the condition
"""
def conditional_login_required(view_func, condition):
    def wrapper(request, *args, **kwargs):
        if condition(request):
            return login_required(view_func)(request, *args, **kwargs)
        else:
            return view_func(request, *args, **kwargs)
    return wrapper


def my_view(request):
    @conditional_login_required(lambda r: r.method == 'POST')
    def view(request):
        # handle both get and post requests
        ...
    return view(request)
"""