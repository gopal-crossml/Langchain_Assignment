"""
Run all examples from one file.
"""

from agents.multi_tools import multi_agent
from agents.single_tool import agent
from agents.api_agent import api_agent

if __name__ =="__main__":
    math_result = agent.invoke({"messages": [{"role": "user", "content": "What is (234 * 12) + 98?"}]})
    print("\n--- Example 1 ---")
    print(math_result["messages"][-1].content)    

    analyzer_result = agent.invoke({"messages": [{"role": "user", "content":"Analyze this paragraph: I love this product. It is excellent!"}]})
    print("\n--- Example 2 ---")
    print(analyzer_result["messages"][-1].content)
    
    date_result = agent.invoke({"messages": [{"role": "user", "content":"What will be the date 45 days from today?"}]})
    print("\n--- Example 3 ---")
    print(date_result["messages"][-1].content)
   

    shipping_result = multi_agent.invoke({"messages": [{"role": "user", "content": "Calculate the total cost if I buy 3 items priced at 499 each,and tell me the delivery date if shipping takes 7 days."}]})
    print("\n--- Multi Tool Example ---")
    print(shipping_result["messages"][-1].content)

    api_result = api_agent.invoke({"messages": [{"role": "user", "content": "How is the weather in Chennai?"}]})
    print("\n--API example--")
    print(api_result["messages"][-1].content)

                                    

