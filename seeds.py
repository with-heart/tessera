from tessera import db
from tessera.lib.models import *

db.create_all()

testadmin = User("testadmin", "test@example.com", "test", "Test Testerson II")
test = User("test", "test1@example.com", "test", "Test Testerson")
db.session.add(testadmin)
db.session.add(test)
db.session.commit()

a_team = Team("The A Team")
a_team.team_lead = test
db.session.add(a_team)
db.session.commit()

testp = Project("TEST", "Test Project")
testp.project_lead = testadmin
a_team.projects.append(testp)

for i in range(100):
    t = Ticket(testp.pkey + "-" +
               str(Project.query.filter_by(pkey=testp.pkey).first().tickets.count() + 1),
        "This is test ticket #" + str(i + 1), "This isn't helplful")

    testp.tickets.append(t)

db.session.add(a_team)
db.session.add(testp)
db.session.commit()