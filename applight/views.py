from idlelib.rpc import request_queue
from django.contrib import messages

from django.shortcuts import render, get_object_or_404

from applight.models import(
    Header,
    About,
    Video,
    FeaturesMain,
    Team,
    Testimonial,
    FAQ,
    Block,
    Contact,
    FormSubmission
)


def index(request):
    if request.method == "POST":
        full_name = request.POST.get("full-name")
        email=request.POST.get("email")
        subject=request.POST.get("subject", "")
        message=request.POST.get("message")

        FormSubmission.objects.create(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, "Your message has been sent successfully!!!")

    banner = get_object_or_404(Header)
    about=About.objects.all()
    video=get_object_or_404(Video)
    features=get_object_or_404(FeaturesMain)
    features_items=features.items.all()
    team=Team.objects.all()
    testimonial=Testimonial.objects.all()
    faq=FAQ.objects.all()
    block=Block.objects.all()
    contact=Contact.objects.first()

    data={
        "banner": banner,
        "about": about,
        "video": video,
        "features": features,
        "features_items": features_items,
        "team": team,
        "testimonial": testimonial,
        "faq": faq,
        "block": block,
        "contact":contact
    }
    return render(request, "base.html", data )

