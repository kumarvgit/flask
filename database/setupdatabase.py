from basic_db import db, Puppy

# Create all table
db.create_all()

sam = Puppy(name='Sammy', age=3)
frank = Puppy(name='Frankie', age=4)

print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])
db.session.commit()

print(sam.id)
print(frank.id)

if __name__ == '__main__':
    print(f'running from main')
else:
    print(f'running as module')
