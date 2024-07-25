//lecture management System 
// for at least details of 5 lecturers.
/*Data members: 
a) Name of the lecturer 
b) Name of the subject 
c) Name of course 
d) Number of lecturers 
Data functions:  
a) To assign initial values  
b) To add a lecture details  
c) To display name and lecture details*/

#include<iostream>
using namespace std;

class Lecture{
	
	private:
				//data members
		string lecturername;
		string subjectname;
		string coursename;
		int no_of_lectures;
		
	public:
				//member functions
				
						//constructor To assign initial values 
		Lecture(string lecturer="", string subject="", string course="", int lectures=0)
		{
			lecturername = lecturer;
			subjectname = subject;
			coursename = course;
			no_of_lectures = lectures;
		}
		
						//function for add a lecture details 
		Addlecture(string lecturer, string subject, string course, int lectures)
		{
			lecturername = lecturer;
			subjectname = subject;
			coursename = course;
			no_of_lectures = lectures;
		}
		
						//function for display name and lecture details
		Displaylecture()
		{
			cout<<"Lecturer Name      : "<<lecturername<<endl;
			cout<<"Subject  Name      : "<<subjectname<<endl;
			cout<<"Course   Name      : "<<coursename <<endl;
			cout<<"Number of Lectures : "<<no_of_lectures<<endl;
		}
};


main()
{
	int lecturer_number,i,lectures;
	string lecturer,subject,course;
				
				//user input for how many details for lecturer user wnats to enter
				
	cout<<"Enter the number of lecturers : ";
	cin>>lecturer_number;

				//create dynamic array for objects of class.
	Lecture* lecturers = new Lecture[lecturer_number];
	
	for(i=0; i<lecturer_number; i++)
	{
		cout<<endl<<"Please Enter Lecturer Deatails : "<<endl;
		cout<<i+1<<".";
		cin.ignore();
		cout<<" Enter Lecturer Name      : ";
		getline(cin,lecturer);
		cout<<"   Enter Subject  Name      : ";
		getline(cin,subject);
		cout<<"   Enter Course   Name      : ";
		getline(cin,course);
		cout<<"   Enter Number of Lectures : ";
		cin>>lectures;
		
				//call the member function for add a lecture details 
		lecturers[i].Addlecture(lecturer,subject,course,	lectures);		
	}
	
	
	cout<<endl<<endl<<"----- Lecturers Deatalis -----"<<endl;
	for(i=0; i<lecturer_number; i++)
	{
		cout<<endl<<"Lecturer "<<i+1<<" Details : "<<endl;
		
				//call the member function for display a lecture details 
		lecturers[i].Displaylecture();	
	}
				// Deallocate the dynamic array
	delete[] lecturers;
}


