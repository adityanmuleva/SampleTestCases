import unittest
import coverage

if __name__ == "__main__":
    # Start coverage measurement
    cov = coverage.Coverage(source=["your_project_folder"])  
    cov.start()

    # Load and run tests
    loader = unittest.TestLoader()
    suite = loader.discover("tests")

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Stop coverage and save the report
    cov.stop()
    cov.save()

    # Generate an XML report for SonarQube
    cov.xml_report(outfile="coverage.xml")

    # Exit based on test success
    exit(0 if result.wasSuccessful() else 1)
