#include <bits/stdc++.h>
using namespace std;

int main(){
#ifndef ONLINE_JUDGE 
	freopen("input1.txt","r" ,stdin);

    freopen("output1.txt","w" ,stdout);
#endif

#include<bits/stdc++.h>
using namespace std;

    int x=0,a=0;
    cin>>a;

    while(a--){
        string s;
        cin >> s;
        if(s[0] == '+')
              x++;
        if(s[0] == '-')
              x--;
        if(s[2] == '+')
              x++;
        if(s[2] == '-')
            x--;
    }
    cout << x << endl;
    return 0;
}

