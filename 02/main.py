import json
import time


def parse_json(json_str: str, required_fields=None,
               keywords=None, keyword_callback=None):
    try:
        json_doc = json.loads(json_str)

        try:
            for field in required_fields:
                value = json_doc[field]

                try:
                    for keyword in keywords:
                        if keyword in value:

                            try:
                                keyword_callback(keyword, field)
                            except TypeError:
                                print("No keyword_callback")

                except TypeError:
                    print("No keywords or value is not string")

        except TypeError:
            print("No required_fields")

    except ValueError:
        print("Wrong json")


def mean(k):
    def decorator(func):
        times = []

        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            times.append(execution_time)
            if len(times) < k:
                average_time = sum(times) / len(times)
            else:
                average_time = sum(times[-k:]) / k
            print(f'Average time for last {k} calls: {average_time} s')

        return wrapper

    return decorator


@mean(3)
def my_function(keyword, field):
    time.sleep(0.1)
    print(f'There is a keyword "{keyword}" in the field "{field}"')
