import { expect } from 'chai';
import sinon from 'sinon';
import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
    const queue = createQueue();

    before((done) => {
        queue.testMode.enter();
        done();
    });

    afterEach((done) => {
        queue.testMode.clear();
        done();
    });

    after((done) => {
        queue.testMode.exit();
        done()
    });

    it('should display an error message if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
    });

    it('should create two new jobs to the queue', (done) => {
        const jobs = [
            { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
            { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' }
        ];

        const mockCreate = sinon.stub(queue, 'create').callsFake((type, data) => {
          const job = {
            type,
            data,
            save: function (callback) {
              callback(null);
              this.id = jobs.indexOf(data) + 1;
            },
            on: function (event, callback) {
              if (event === 'complete') callback;
              if (event === 'failed') callback(new Error('Job failed'));
              if (event === 'progress') callback(50);
            }
          };
          return job;
        });

        createPushNotificationsJobs(jobs, queue);

        setTimeout(() => {
          expect(queue.testMode.jobs.length).to.equal(2);
          expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
          expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
          expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
          expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
          done();
        }, 500);
    });
});
