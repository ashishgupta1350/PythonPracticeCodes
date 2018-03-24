#include <iostream>
#include <cstring>
#include <stack>
#include <algorithm>
#define flag '#'

using namespace std;

bool isOperator(char c)
{
    /// c is the incoming character
	if(c=='+' || c=='-' || c=='*' || c=='/' || c=='^' || c=='$')
	return true;
	else
	return false;
}

int main()
{
	stack<char> myStack;
	char postfix[30], prefix[30];
	int j=0,len;
	cout<<"Input a postfix expression  : ";
	cin>>postfix;
	len = strlen(postfix);
	for(int i=len-1;i>=0;i--)
	{
		if(isOperator(postfix[i]))
		myStack.push(postfix[i]);
		else
		{
			prefix[j++] = postfix[i];
			while(!myStack.empty() && myStack.top()==flag)
			{
				myStack.pop();
				prefix[j++] = myStack.top();
				myStack.pop();
			}
			myStack.push(flag);

		}
	}
	prefix[j] = 0;
	reverse(prefix, prefix + len);
	cout<<"The prefix expression is  : "<<prefix;
	return 0;
}
