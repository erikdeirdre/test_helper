# testhelper

A class to help with response, request, and expected results

## How to Use

The class accepts 'text' and 'json' based files for storing response and request messages as well as Graphql variables.

```bash
tests
|
|- files
|    |- test name
|    |     |- expected_results.json
|    |     |- send_request.txt
|    |     |- variables.txt (optional)
|    |- test name 2
|    |
|- test file

```

`TestHelper` constructor expects two arguments: an absolute directory path, and a test name.

`TestHelper` concatenates the arguments to create the directory to load the files from. The class loads three files. A request file, `send_request.{file type}`; a response file, `expected_results.{file type}`; and an optional variables file, `variables.{file type}`.

## Example

The following code illustrates how to use `TestHelper` to test a Graphql query.

```python
    def test_query(self):
        test_data = TestHelper(self.dir_name,
        # The following line captures the test name, 'test_query' from the
        # function name.
                              sys._getframe(  ).f_code.co_name)

        test_data.load_files()

        executed = self.client.execute(test_data.get_send_request())

        self.assertEqual(loads(dumps(executed['data'])),
                         test_data.get_expected_result()['data'])
```

The pattern allows for quick test creation via cut-and-paste of the test function and change the test name.
