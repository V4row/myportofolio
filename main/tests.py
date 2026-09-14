from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Skill, Project


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            # title="Mentor DDP0 2026",
            # description="Membantu mahasiswa baru Fakultas Ilmu komputer mempelajari dasar python dan kehidupan di kampus",
            category="part-time",
        )
        self.skill = Skill.objects.create(
            title="Python",
            percentage=73,
        )
        self.project = Project.objects.create(
            title="Portfolio Website",
            description="Website portofolio pribadi berbasis Django.",
            url="https://github.com/V4row/myportofolio",
            thumbnail="https://imgs.search.brave.com/1aOiulsLZPYMzvIzhp89C9wu4hBaR98upwX1bNndR1w/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/bWFnbmlmaWMuY29t/L3ByZW1pdW0tdmVj/dG9yL2R1cGxpY2F0/ZS1jb3B5LWRvY3Vt/ZW50LWljb25zLWlz/b2xhdGVkLXdoaXRl/LWJhY2tncm91bmRf/NzU5MzEyLTExMjU0/LmpwZz9zZW10PWFp/c190ZXN0X2Mmdz03/NDAmcT04MA"
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

    def test_skill_model(self):
        self.assertEqual(str(self.skill), "Python")
        self.assertEqual(self.skill.percentage, 73)

    def test_skills_page(self):
        response = self.client.get(reverse("main:show_skill"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skill.html")
        self.assertContains(response, self.skill.title)
        self.assertContains(response, f"{self.skill.percentage}%")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_skills_page(self):
        Skill.objects.all().delete()
        response = self.client.get(reverse("main:show_skill"))

        self.assertContains(response, "Belum ada skill yang ditambahkan.")


    def test_project_model(self):
        self.assertEqual(str(self.project), "Portfolio Website")
        self.assertEqual(self.project.url, "https://github.com/V4row/myportofolio")

    def test_project_page_with_thumbnail(self):
        response = self.client.get(reverse("main:show_project"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")
        self.assertContains(response, self.project.title)
        self.assertContains(response, self.project.description)
        self.assertContains(response, self.project.url)
        self.assertContains(response, self.project.thumbnail)
        self.assertNotContains(response, "NO IMAGE AVAILABLE")

    def test_project_page_without_thumbnail(self):
        self.project.thumbnail = None
        self.project.save()
        response = self.client.get(reverse("main:show_project"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.project.title)
        self.assertContains(response, "NO IMAGE AVAILABLE")

    def test_empty_project_page(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:show_project"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "COMING SOON.")