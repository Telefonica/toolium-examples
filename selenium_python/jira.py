# -*- coding: utf-8 -*-
'''
(c) Copyright 2014 Telefonica, I+D. Printed in Spain (Europe). All Rights
Reserved.

The copyright to the software program(s) is property of Telefonica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefonica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
'''
import logging
import urllib2
import re

# Configure logger
logger = logging.getLogger(__name__)

# Base url of the test execution service
JIRA_EXECUTION_URL = 'http://qacore02.hi.inet/jira/test-case-execution'


def jira(test_key):
    '''
    Decorator to update test status in Jira
    '''
    def decorator(test_item):
        def modified_test(*args, **kwargs):
            try:
                test_item(*args, **kwargs)
            except Exception as exc:
                change_jira_status(test_key, 'Fail')
                raise exc
            change_jira_status(test_key, 'Pass')
        return modified_test
    return decorator


def change_jira_status(test_key, test_status):
    '''
    Update test status in Jira
    '''
    logger.info("Updating Test Case '{0}' in Jira with status {1}".format(test_key, test_status))
    jira_execution_url = '{0}?jiraTestCaseId={1}&jiraStatus={2}'
    try:
        response = urllib2.urlopen(jira_execution_url.format(JIRA_EXECUTION_URL, test_key, test_status))
        logger.debug(response.read().strip(' \t\n\r'))
        response.close()
    except urllib2.HTTPError as exc:
        # Extract error message from the HTTP response
        message = re.search('.*<u>(.*)</u></p><p>.*', exc.read())
        if message:
            error_message = message.group(1)
        else:
            message = re.search('.*<title>(.*)</title>.*', exc.read())
            if message:
                error_message = message.group(1)
        logger.warn("Error updating Test Case '{0}': [{1}] {2}".format(test_key, exc.code, error_message))
    except urllib2.URLError as exc:
        logger.warn("Error updating Test Case '{0}': {1}".format(test_key, exc.reason))
