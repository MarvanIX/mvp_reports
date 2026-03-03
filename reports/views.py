from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import MagicLink, Report, Company


@login_required
def home(request):
    return render(request, 'reports/home.html')

@login_required
def company_view(request):
    if request.method == "POST":
        company_id = request.POST.get("company_id")
        name = request.POST.get("name")
        delete_id = request.POST.get("delete_id")  # DELETE

        if delete_id:  # DELETE
            company = Company.objects.get(id=delete_id, managers=request.user)
            company.delete()
            return redirect("company")

        elif company_id:  # EDIT
            company = Company.objects.get(id=company_id, managers=request.user)
            company.name = name
            company.save()
            return redirect("company")

        else:  # CREATE
            company = Company.objects.create(name=name)
            company.managers.add(request.user)
            return redirect("company")

    # get companies for this user
    companies = request.user.companies.all()

    # ensure each company has a magic link
    for company in companies:
        if not hasattr(company, "magic_link"):
            MagicLink.objects.create(company=company)

    return render(request, "reports/company.html", {
        "companies": companies
    })
@login_required
def reports_view(request):
    # get companies managed by current user
    companies = request.user.companies.all()

    # get all reports for those companies
    reports = Report.objects.filter(company__in=companies).order_by("-created_at")

    return render(request, "reports/reports.html", {
        "reports": reports
    })
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
        # Notify all managers of the company about the new report
        # for manager in company.managers.all():
        #     send_mail(
        #         subject="New Report Submitted",
        #         message=f"A new report was submitted for {company.name}",
        #         from_email="noreply@yourapp.com",
        #         recipient_list=[manager.email],
        #     )
        return render(request, "reports/success.html")

    return render(request, "reports/submit_report.html", {"company": company})

