"""
Portfolio Backend Script - Hafizh Zuhdi Hartanto
Fakultas Ilmu Komputer, Universitas Indonesia
"""

class StudentProfile:
    def __init__(self, name, npm, program, faculty, university):
        self.name = name
        self.npm = npm
        self.program = program
        self.faculty = faculty
        self.university = university
        self.skills = []
        self.education_history = []

    def add_skill(self, skill_name, category, description):
        self.skills.append({
            "name": skill_name,
            "category": category,
            "description": description
        })

    def add_education(self, institution, degree, period, achievements):
        self.education_history.append({
            "institution": institution,
            "degree": degree,
            "period": period,
            "achievements": achievements
        })

    def display_info(self):
        print(f"=== PROFILE: {self.name} ===")
        print(f"NPM: {self.npm}")
        print(f"Program: {self.program}")
        print(f"Faculty: {self.faculty}")
        print(f"University: {self.university}\n")

        print("=== EDUCATION ===")
        for edu in self.education_history:
            print(f"- {edu['institution']} ({edu['degree']}) | {edu['period']}")
            for ach in edu['achievements']:
                print(f"  * {ach}")

        print("\n=== SKILLS ===")
        for skill in self.skills:
            print(f"- [{skill['category']}] {skill['name']}: {skill['description']}")


def initialize_hafizh_profile():
    hafizh = StudentProfile(
        name="Hafizh Zuhdi Hartanto",
        npm="2506656785",
        program="S1 Ilmu Komputer",
        faculty="Fasilkom",
        university="Universitas Indonesia"
    )

    # Education Data
    hafizh.add_education(
        institution="Universitas Indonesia",
        degree="S1 Ilmu Komputer",
        period="2025 - Sekarang",
        achievements=[
            "Aktif mengikuti perkuliahan CS, Cloud, dan Operating Systems.",
            "Eksplorasi pemrograman Python, C++, dan logika digital.",
            "Kepanitiaan fakultas (Open House Fasilkom UI & Social Project)."
        ]
    )

    hafizh.add_education(
        institution="SMAN 1 Bekasi",
        degree="MIPA",
        period="2022 - 2025",
        achievements=[
            "Lulusan SMAN 1 Bekasi angkatan 2025.",
            "Juara 1 Olimpiade TIK-Informatika Nasional (OTN) E-sports 2023.",
            "Juara 2 Cyber Competition XV 2024 se-Jabar & DKI Jakarta."
        ]
    )

    # Skills Data
    hafizh.add_skill(
        skill_name="Basic Programming & Logic",
        category="DDP 1",
        description="Pemrograman prosedural, problem solving, dan kontrol alur Python."
    )

    hafizh.add_skill(
        skill_name="Object-Oriented Programming",
        category="DDP 1",
        description="Penerapan Class, Object, Inheritance, dan Encapsulation di Python."
    )

    hafizh.add_skill(
        skill_name="Digital Systems & Logic Design",
        category="PSD",
        description="Sirkuit logika, Multiplexer, Decoder, Register, dan simulasi FSM."
    )

    return hafizh


if __name__ == "__main__":
    profile = initialize_hafizh_profile()
    profile.display_info()