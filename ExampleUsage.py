import magnumbi_depot
import logging
import platform
import sys

if __name__ == '__main__':
    # Logger
    logging.basicConfig(level=logging.DEBUG, format='{0} %(name)s [%(levelname)s]  %(asctime)s: %(message)s'.format(
        str(platform.node())))
    logging.info("Microservice Client Tester Launched with %s", str(sys.argv))

    # Tests stuff
    client = magnumbi_depot.DispatchClient(
        uri='https://127.0.0.1',
        port=6883,
        access_key='test',
        secret_key='token',
        ssl_verify=False
    )

    # Check status of server
    status_result = client.check_status()
    if not status_result:
        logging.info('Status request not successful!')
        exit(404)
    else:
        logging.info('Status check completed successfully.')

    # Check app job queue is empty
    empty = client.is_empty('TEST')
    logging.info('Is queue empty: %s', str(empty))

    # Submit job
    client.submit_job('TEST', {'TEST': 'DATA'})
    logging.info('Submit successful')

    # Request job
    job_result = client.request_job('TEST', job_timeout=8, request_timeout=-1)
    if job_result:
        logging.info('Job request successful %s', str(job_result))
    elif job_result is None:
        logging.info('No job found!')

    # Complete job
    if job_result:
        client.complete_job('TEST', job_result.job_id)
        logging.info('Complete successful')
    else:
        logging.warn('No job found to complete!')

    # Get and complete all jobs
    job_result = client.request_job('TEST', job_timeout=8, request_timeout=-1)
    while job_result:
        client.complete_job('TEST', job_result.job_id)
        job_result = client.request_job('TEST', job_timeout=8, request_timeout=-1)
    logging.info('Clear done!')

    # Last thing
    logging.info('Complete!')
