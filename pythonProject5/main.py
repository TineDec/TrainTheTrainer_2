from matplotlib import pyplot as plt

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]

plt.xlabel('CoGent Partners')
plt.ylabel('Aantal Ontsloten Records')

plt.plot(instellingen, aantal_records)
plt.show()
