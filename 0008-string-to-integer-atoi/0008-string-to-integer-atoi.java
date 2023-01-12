class Solution {
    public int myAtoi(String s) {
        int i=0;
        boolean negative=false;
        while(i<s.length()&&s.charAt(i)==' '){
            i++;
        }
        if(i<s.length()&&(s.charAt(i)=='-'||s.charAt(i)=='+')){
            if(s.charAt(i)=='-')
                negative=true;
            i++;
        }
        int size=0;
        while (i<s.length()){
            if ((s.charAt(i)-'0')<0||(s.charAt(i)-'0')>9)
                break;
            size++;
            i++;
        }
        i--;
        int res=0;
        for (int j = 0; j < size; j++) {
            res+=negative?-(s.charAt(i)-'0')*Math.pow(10,j):(s.charAt(i)-'0')*Math.pow(10,j);
            i--;
        }
        return res;
    }
}