//banking System bole to jakkass

#include<iostream>
using namespace std;

class Bank_Accout{
		
	string name;
	int accountno;
	int deposit;
	int withdraw;
	int balance;
		
	public:
				
		Bank_Accout()		//constructor
		{
			balance = 0;
			cout<<"JAKAASS BANK me Aapka Svagat he....."<<endl<<endl;
		}
			
			//getter method and setter methods
		getname(string name)
		{
			this->name = name;
		}
		setname()
		{
			cout<<"NAME            : "<<this->name<<endl;
		}	
		getaccountno(int accountno)
		{
			this->accountno = accountno;
		}
		setaccountno()
		{
			cout<<"Account No      : "<<this->accountno<<endl;
		}
		getdeposit(int deposit)
		{
			this->deposit = deposit;	
		}
		getwithdraw(int withdraw)
		{
			this->withdraw = withdraw;
		}
		setbalance()
		{
			cout<<"current Balance : "<<balance<<endl;
		}
		
		deposit_amount()		//function for deposit amount
		{
			balance += this->deposit;
			cout<<"Paisa Deposit Succeffully."<<endl;
			cout<<"Current balance : "<<balance<<endl<<endl;
		}
		
		withdraw_amount()		//function for withdraw amount
		{
			if(this->withdraw>balance)		//check availbility
			{
				cout<<"Aapke account me Paryapt balance nahi he....";
			}
			else
			{
				balance -= this->withdraw;
				cout<<"Withdraw Successfully."<<endl;
				cout<<"Current balance : "<<balance<<endl<<endl;
			}
		}
};

main()
{
	Bank_Accout ba;				//object creation
		
			//user inputs
		string name;
		int accountno,ch,withdraw,deposit;
		
		cout<<"Enter Account Holder's Name : ";
		getline(cin,name);
		ba.getname(name);
		cout<<"Enter Account Number        : ";
		cin>>accountno;
		ba.getaccountno(accountno);
		
		while(ch!=3)
		{						
			cout<<endl<<"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"<<endl<<endl;
			cout<<"Aap Kya karna chahenge?"<<endl<<"krupya koi Ek viklap chuniye..."<<endl<<endl;
			cout<<"1.Deposit Amount  "<<endl;
			cout<<"2.Withdraw Amount "<<endl;
			cout<<"3.Display and Exit"<<endl<<endl;
			cout<<"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"<<endl<<endl;
			
			cout<<"Enter your Choice : ";
			cin>>ch;
			
			switch(ch)
			{
				case 1:
					cout<<endl<<"++++++++++++++++++++++++++++++++++"<<endl<<endl;
					cout<<"Enter Deposit Amount : ";
					cin>>deposit;
					ba.getdeposit(deposit);
					ba.deposit_amount();
					cout<<endl<<"++++++++++++++++++++++++++++++++++"<<endl<<endl;
					break;
					
				case 2:
					cout<<endl<<"----------------------------------"<<endl<<endl;
					cout<<"Enter Withdraw Amount : ";
					cin>>withdraw;
					ba.getwithdraw(withdraw);
					ba.withdraw_amount();
					cout<<endl<<"----------------------------------"<<endl<<endl;
					break;
					
				case 3:
					cout<<endl<<"________ Person's Details ________"<<endl<<endl;
					ba.setname();
					ba.setaccountno();
					ba.setbalance();
					cout<<endl<<"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"<<endl<<endl;
					cout<<"Thank you so much for use our system.."<<endl;
					cout<<"Apaka Din Shubh rahe...."<<endl<<endl;
					cout<<"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"<<endl;
					break;
					
				default:
					cout<<"Invalid Choice........"<<endl;
					cout<<"Please Enter right choice.."<<endl;
					cout<<"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"<<endl;
			}
		}
}


