class Project:
    def __init__(self, name, duration_method, tech_stack, max_team_size=5):
        self.name = name
        self.duration_method = duration_method
        self.tech_stack = tech_stack
        self.max_team_size = max_team_size
        self.team = []

    def get_team_by_level(self, level):
        return [ashu for ashu in self.team if ashu.get_level().lower() == level.lower()]

    def get_team_by_skill(self, skill):
        return [ashu for ashu in self.team if skill.lower() in map(str.lower, ashu.skills)]

    def add_team_member(self, member):
        if len(self.team) >= self.max_team_size:
            print(f"❌ Cannot add {member.name}. Team is full ({self.max_team_size} members).")
        else:
            self.team.append(member)

    def show_team(self):
        print(f"👥 Team members for {self.name}:")
        for ashu in self.team:
            print(f"- {ashu.name} ({ashu.get_level()})")

    def details(self):
        return f"Project Name: {self.name}, Duration Method: {self.duration_method}, Tech Stack: {', '.join(self.tech_stack)}"

    def summary_report(self):
        levels = {"Junior": 0, "Associate": 0, "Senior": 0, "Lead": 0}
        skills_set = set()

        for ashu in self.team:
            levels[ashu.get_level()] += 1
            skills_set.update([skill.lower() for skill in ashu.skills])

        print(f"\n📊 Summary for Project: {self.name}")
        print("Developer Levels:")
        for level, count in levels.items():
            print(f"  - {level}: {count}")
        print(f"Skills Covered: {', '.join(sorted(skills_set)) if skills_set else 'No skills added yet'}")

    def __str__(self):
        return self.name


class Developer:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience
        self.projects = []
        self.skills = []

    def assign_project(self, project):
        self.projects.append(project)
        project.add_team_member(self)

    def information(self):
        print(f"👤 Name: {self.name}")
        print(f"📅 Experience: {self.experience} years")
        print(f"📁 Projects: {', '.join([proj.name for proj in self.projects]) if self.projects else 'No projects assigned'}")
        print(f"🛠️ Skills: {', '.join(self.skills) if self.skills else 'Not added yet'}")
        print(f"🏷️ Level: {self.get_level()}")
        for proj in self.projects:
            print(f"🔍 Project Details: {proj.details()}")

    def add_skills(self, skills):
        self.skills = skills

    def get_level(self):
        if self.experience < 2:
            return "Junior"
        elif 2 <= self.experience < 5:
            return "Associate"
        elif 5 <= self.experience < 10:
            return "Senior"
        else:
            return "Lead"
        
    def suggest_developers(self, required_skills):
        print(f"🔍 {self.name} suggests developers with skills: {', '.join(required_skills)}")


class SeniorDeveloper(Developer):
    def lead_team(self):
        for proj in self.projects:
            print(f"🧑‍💼 {self.name} is leading the team on {proj.name}.")


class JuniorDeveloper(Developer):
    def assist_team(self):
        for proj in self.projects:
            print(f"👨‍💻 {self.name} is assisting the team on {proj.name}.")


# 🏗️ Projects
ai_project = Project("AI Development", "Agile", ["Python", "TensorFlow", "Keras"], max_team_size=3)
web_project = Project("Web Development", "Waterfall", ["HTML", "CSS", "JavaScript"], max_team_size=2)

# 👨‍💻 Developers
ashwani = SeniorDeveloper("Ashwani", 6)
ashwani.add_skills(["Python", "ML", "TensorFlow"])
ashwani.assign_project(ai_project)

rahul = SeniorDeveloper("Rahul", 7)
rahul.add_skills(["Python", "NLP"])
rahul.assign_project(ai_project)

john = JuniorDeveloper("John", 1)
john.add_skills(["HTML", "CSS"])
john.assign_project(web_project)

# 📋 Developer Info
ashwani.information()
ashwani.lead_team()

print("\n--------------------------\n")

john.information()
john.assist_team()

print("\n--------------------------\n")


print("🎯 Senior Developers in AI Project:")
seniors = ai_project.get_team_by_level("Senior")
for ashu in seniors:
    print(f"- {ashu.name}, Experience: {ashu.experience} years")

print("\n🔎 Developers in AI Project with Python skill:")
python_devs = ai_project.get_team_by_skill("Python")
for ashu in python_devs:
    print(f"- {ashu.name}, Skills: {', '.join(ashu.skills)}")

print("\n🎯 Junior Developers in Web Project:")
juniors = web_project.get_team_by_level("Junior")  
for ashu in juniors:
    print(f"- {ashu.name}, Experience: {ashu.experience} years")

ai_project.summary_report()  
web_project.summary_report()  