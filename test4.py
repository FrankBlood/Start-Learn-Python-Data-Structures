ab={'Swaroop':'sakdfjksa','Larry':'dasfsf','Guoxiu He':'dsfaaf','Xu Dong':'dsadf'}
print("Swaroop's address is %s" %ab['Swaroop'])
ab['Dan Zheng']='sdaljsjlg'
del ab['Guoxiu He']
print('\nThere are %d contacts in the address-book' %len(ab))
for name,address in ab.items():
	print('Contacts %s at %s' %(name,address))
if 'Xu Dong' in ab:
	print('\nXu Dong address is %s' %ab['Xu Dong'])