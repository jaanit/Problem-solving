#include <iostream>
#include <stack>
#include <deque>

int main() {
    int t;
    std::cin >> t;
    std::stack<int, std::deque<int> > stack;
    std::deque<std::string> output;

    for (int i = 0; i < t; ++i) {
        int queryType;
        std::cin >> queryType;
        if (queryType == 1) {
            int n;
            std::cin >> n;
            stack.push(n);
        } else if (queryType == 2) {
            if (!stack.empty()) {
                stack.pop();
            }
        } else if (queryType == 3) {
            if (!stack.empty()) {
                output.push_back(std::to_string(stack.top()));
            } else {
                output.push_back("Empty!");
            }
        }
    }

   for (size_t i = 0; i < output.size(); ++i) {
    std::cout << output[i] << "\n";
}

    return 0;
}
