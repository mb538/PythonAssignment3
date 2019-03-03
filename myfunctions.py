def get_eng_speaker_amount(dataset, year): 
    native_eng_mask = (dataset[:,0] == year) & ((dataset[:,3] == 5170) | (dataset[:,3] == 5502))
    native_eng = sum(dataset[native_eng_mask][:,4])

    non_native_eng_mask = (dataset[:,0] == year) & ((dataset[:,3] != 5170) & (dataset[:,3] != 5502))
    non_native_eng = sum(dataset[non_native_eng_mask][:,4])
    
    return native_eng, non_native_eng

def filter_dataset(dataset, mask): 
    return dataset[mask]

def get_age_groups(dataset):
    age_groups = {}
    for i in range(0, 100, 10):
        age_mask = ((dataset[:,2] >= i) & (dataset[:,2] <= i+10))
        people = filter_dataset(dataset, age_mask)[:,4].sum()
        age_groups[str(i) + '-' + str(i+10)] = people
    return age_groups

def get_accumulated_population(dataset, x):
    people_acc = []
    if x == 'year':
        years = list(set(dataset[:,0]))
        for y in years: 
            people_in_year = dataset[(dataset[:,0] == y)]
            sum_of_people = people_in_year[:,4].sum()
            people_acc.append(sum_of_people)
        return people_acc, years
    elif x == 'neighbourhood':
        neighbourhoods = list(set(dataset[:,1]))
        for n in neighbourhoods: 
            people_in_n = dataset[(dataset[:,1] == n)]
            sum_of_people = people_in_n[:,4].sum()
            people_acc.append(sum_of_people)
        return people_acc, neighbourhoods
    elif x == 'age':
        ages = list(set(dataset[:,2]))
        for a in ages: 
            people = dataset[(dataset[:,2] == a)]
            sum_of_people = people[:,4].sum()
            people_acc.append(sum_of_people)
        return people_acc, ages
    elif x == 'nationality':
        nationalities = list(set(dataset[:,3]))
        for n in nationalities: 
            people = dataset[(dataset[:,3] == n)]
            sum_of_people = people[:,4].sum()
            people_acc.append(sum_of_people)
        return people_acc, nationalities
    else:
        return people_acc