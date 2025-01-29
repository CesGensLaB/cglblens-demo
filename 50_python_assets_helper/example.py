import os
from cglblens import StandaloneTaskRunner
from cglblens.helpers.assets import Assets

TEST_DIR = os.path.dirname(os.path.realpath(__file__))

def setup_assets():
    # Setup Assets Helper with the target folder
    assets = Assets(
        os.path.join(TEST_DIR, "test_assets"), force_clean=True, force_create=True
    )

    # Copy the tree where we found report of cglblens
    assets.copy(assets.report_discover(TEST_DIR))

    # Create an index of those reports
    assets.create_html_index(
        os.path.join(assets.path, "index.html"),
        assets.path,
        assets.report_get_name(),
    )

def run_generic_test(input_dir):
    test_dir = os.path.join(TEST_DIR, input_dir)
    runner = StandaloneTaskRunner(f"{TEST_DIR}/cglblens.yml")
    results = runner.process(test_dir, origin_working_dir=test_dir)

    if results.error:
        raise Exception(results.error)
    else:
        assert (
            not results.processor_results.errors
            and not results.processor_results.warnings
        )

if __name__ == "__main__":
    run_generic_test("example_1")
    run_generic_test("example_2")
    setup_assets()
    print("Test completed successfully.")