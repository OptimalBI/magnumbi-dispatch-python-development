import magnumbi_depot
import logging
import platform
import sys

if __name__ == '__main__':
    # Logger
    logging.basicConfig(level=logging.DEBUG, format='{0} %(name)s [%(levelname)s]  %(asctime)s: %(message)s'.format(
        str(platform.node())))
    logging.info("Microservice Client Tester Launched with %s", str(sys.argv))

    # Make the magnumbi dispatch library be quiet unless something goes wrong.
    logging.getLogger("magnumbi_dispatch").setLevel(logging.WARNING)

    # Lets create a DispatchClient.
    client = magnumbi_depot.DispatchClient(
        uri='https://127.0.0.1',
        port=6883,
        access_key='test',
        secret_key='token',
        ssl_verify=False
    )

    app_id = 'test_app_id'

    # Check status of server
    logging.info('Checking status of the MagnumBI Dispatch Server')
    status_result = client.check_status()
    if not status_result:
        logging.info('Status request not successful!')
        exit(404)
    else:
        logging.info('Status check completed successfully.')

    # Check app job queue is empty, it should be for this example.
    empty = client.is_empty(app_id)
    logging.info('Is queue empty: %s', str(empty))

    # Submit to MagnumBI Dispatch queue.
    logging.info('Submitting new Dispatch Job.')
    client.submit_job(app_id, {'Message': 'Hello'})
    logging.info('Submit successful')

    # Request a job from the system
    logging.info('Requesting a job from MagnumBI Dispatch.')
    job_result = client.request_job(app_id, job_timeout=8, request_timeout=-1)
    if job_result:
        logging.debug('Job request successful %s', str(job_result))
        logging.info(job_result.data['Message'] + ' world!')
    elif job_result is None:
        logging.info('OH NO! No job found!')

    # Mark the job as complete so that the Dispatch server knows we did the tasks and wont assign it to anyone else.
    if job_result:
        client.complete_job(app_id, job_result.job_id)
        logging.info('Complete successful')
    else:
        logging.warning('No job found to complete!')

    # Get and complete all jobs (to clean up the queue)
    job_result = client.request_job('TEST', job_timeout=8, request_timeout=-1)
    while job_result:
        client.complete_job('TEST', job_result.job_id)
        job_result = client.request_job('TEST', job_timeout=8, request_timeout=-1)
    logging.info('Clear done!')

    # Last thing
    logging.info('We are finished!')
