import { createQueue } from 'kue';

const queue = createQueue();

const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error('Notification job failed to create:', err);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('NOtification job failed');
});
