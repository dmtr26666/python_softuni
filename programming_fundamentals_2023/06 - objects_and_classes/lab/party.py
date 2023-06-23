class Party:
    def __init__(self):
        self.people = []

    def add_people(self, person):
        self.people.append(person)

party = Party()

while True:
    name = input()
    if name == 'End':
        break

    party.add_people(name)

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")