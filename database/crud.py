from basic_db import db, Puppy

my_puppy = Puppy(name='Rufus', age=3)
db.session.add(my_puppy)
db.session.commit()

# Get all
all_puppies = Puppy.query.all()
print(all_puppies)

# Get one
puppy_one = Puppy.query.get(1)
print(puppy_one)

# Filters
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie)

# Update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# Delete
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

# Get all
all_puppies = Puppy.query.all()
print(all_puppies)

if __name__ == '__main__':
    print(f'running from main')
else:
    print(f'running as module')
