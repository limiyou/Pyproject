import jsonpath
res = {"code": 0, "msg": "OK",
       "data": {"id": 190, "leave_amount": 0.02, "mobile_phone": "13888888811", "reg_name": "小柠檬",
                "reg_time": "2019-08-27 09:24:03.0", "type": 1}}
print(jsonpath.jsonpath(res,"$..id")[0])  # ..是在任何位置找id
print(jsonpath.jsonpath(res,"$..mobile_phone")[0])