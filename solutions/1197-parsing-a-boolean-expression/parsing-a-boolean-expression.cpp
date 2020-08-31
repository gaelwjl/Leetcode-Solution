// Return the result of evaluating a given boolean expression, represented as a string.
//
// An expression can either be:
//
//
// 	"t", evaluating to True;
// 	"f", evaluating to False;
// 	"!(expr)", evaluating to the logical NOT of the inner expression expr;
// 	"&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner expressions expr1, expr2, ...;
// 	"|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner expressions expr1, expr2, ...
//
//
//  
// Example 1:
//
//
// Input: expression = "!(f)"
// Output: true
//
//
// Example 2:
//
//
// Input: expression = "|(f,t)"
// Output: true
//
//
// Example 3:
//
//
// Input: expression = "&(t,f)"
// Output: false
//
//
// Example 4:
//
//
// Input: expression = "|(&(t,f,t),!(t))"
// Output: false
//
//
//  
// Constraints:
//
//
// 	1 <= expression.length <= 20000
// 	expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f', ','}.
// 	expression is a valid expression representing a boolean, as given in the description.
//
//


class Solution {
public:
  bool parseBoolExpr(string expression) {
    int s = 0;
    return parse(expression, s);
  }
private:  
  bool parse(const string&exp, int& s) {
    char ch = exp[s++];    
    if (ch == 't') return true;      
    if (ch == 'f') return false;
    if (ch == '!') {
      bool ans = !parse(exp, ++s);
      ++s;
      return ans;
    } 
    bool is_and = (ch == '&');
    bool ans = is_and;
    ++s;
    while (true) {
      if (is_and) ans &= parse(exp, s);
      else ans |= parse(exp, s);
      if (exp[s++] == ')') break;
    }
    return ans;
  }
};
