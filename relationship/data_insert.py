from models import db, Puppy, Owner, Toy


db.create_all()

# Creating puppy

rufus = Puppy('Rufus')
fido = Puppy('Fido')

db.session.add_all([rufus, fido])
db.session.commit()

# Check
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()

jose = Owner('Jose', rufus.id)

toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

# Grab Rufus
rufus = Puppy.query.filter_by(name='Rufus')
print(rufus)
rufus.report_toys()


if __name__ == '__main__':
    print(f'running from main')
else:
    print(f'running as module')



