from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import MagicLink, Report
@login_required
def home(request):
    return render(request, 'reports/home.html')



def public_reports(request, token):
    magic_link = get_object_or_404(MagicLink, token=token, is_active=True)
    company = magic_link.company

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        is_anonymous = request.POST.get("anonymous") == "on"
        email = request.POST.get("email") if not is_anonymous else None

        Report.objects.create(
            company=company,
            title=title,
            description=description,
            is_anonymous=is_anonymous,
            email=email
        )

        return render(request, "reports/success.html")

    return render(request, "reports/public_form.html", {"company": company})


@login_required
def manager_reports(request):

    company = request.user.companies.first()

    reports = company.reports.all().order_by("-created_at")

    return render(request, "reports/manager_dashboard.html", {
        "reports": reports
    })