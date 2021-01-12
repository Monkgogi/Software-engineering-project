def set_description(description):
    print(' Choose from the list below which indicate the reasons for coming to london:'
          'Miscellaneous = 0'
          'Study = 1'
          'Visit family and relatives = 2'
          'Business = 3'
          'Holiday = 4')

    reason = ['Miscellaneous', 'Study', 'Visit family and relatives', 'Business', 'Holiday']

    number_of_days = int(input('Enter the number of days you will be staying in London: '))
    n = int(input('Pick reason:'))
    x = reason[n]
    print('Reason: ' + str(x) + ' for ' + str(number_of_days) + ' days')

    return description
