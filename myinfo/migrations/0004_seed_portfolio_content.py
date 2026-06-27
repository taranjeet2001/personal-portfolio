from django.db import migrations


def seed_portfolio(apps, schema_editor):
    PortfolioProfile = apps.get_model("myinfo", "PortfolioProfile")
    ProfileTag = apps.get_model("myinfo", "ProfileTag")
    Experience = apps.get_model("myinfo", "Experience")
    Certification = apps.get_model("myinfo", "Certification")
    Skill = apps.get_model("myinfo", "Skill")

    if PortfolioProfile.objects.exists():
        return

    profile = PortfolioProfile.objects.create(
        full_name="Taranjeet Singh",
        headline="Python Developer | Senior Software Engineer",
        summary=(
            "Python full stack developer with experience in Django, React, REST APIs, "
            "database design, Docker, and ERP-style applications. I like building simple, "
            "reliable software that is easy to maintain."
        ),
        location="Kalkaji, New Delhi",
        email="taranjeet.0815@gmail.com",
        phone="+91 9999-284429",
        linkedin_url="https://www.linkedin.com/in/taranjeet---singh/",
        github_url="https://github.com/taranjeet2001",
        primary_image="portfolio/images/photo5.jpg",
        resume_pdf="portfolio/resumes/Taranjeet-Singh.pdf",
    )

    ProfileTag.objects.bulk_create(
        [
            ProfileTag(profile=profile, label="Python Developer", order=1),
            ProfileTag(profile=profile, label="Senior Software Engineer", order=2),
            ProfileTag(profile=profile, label="Django Developer", order=3),
        ]
    )

    Experience.objects.bulk_create(
        [
            Experience(
                profile=profile,
                period="Sep 2023 - Present",
                title="Software Developer",
                company="SPA Innovision Pvt Ltd",
                description=(
                    "Worked on ERP-style applications, reporting flows, asset tracking, "
                    "and React-based client portals. Focused on clean architecture, API work, "
                    "and performance improvements."
                ),
                order=1,
            ),
            Experience(
                profile=profile,
                period="2023",
                title="Freelance Project",
                company="paslaundry.in",
                description=(
                    "Built custom web application features with Python, Django, HTML, CSS, "
                    "JavaScript, AJAX, and SQLite for a production project."
                ),
                order=2,
            ),
        ]
    )

    Certification.objects.create(
        profile=profile,
        period="2023",
        title="Full Stack Development in Python",
        issuer="Cetpa Infotech Pvt Ltd",
        order=1,
    )

    Skill.objects.bulk_create(
        [
            Skill(profile=profile, name="Python", order=1),
            Skill(profile=profile, name="Django", order=2),
            Skill(profile=profile, name="React", order=3),
            Skill(profile=profile, name="JavaScript", order=4),
            Skill(profile=profile, name="HTML", order=5),
            Skill(profile=profile, name="CSS", order=6),
            Skill(profile=profile, name="REST APIs", order=7),
            Skill(profile=profile, name="Docker", order=8),
            Skill(profile=profile, name="SQL", order=9),
            Skill(profile=profile, name="Git", order=10),
        ]
    )


class Migration(migrations.Migration):

    dependencies = [
        ("myinfo", "0003_alter_portfolioprofile_primary_image_and_more"),
    ]

    operations = [
        migrations.RunPython(seed_portfolio, migrations.RunPython.noop),
    ]
