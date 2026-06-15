import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int jobsLength = jobs.length;

        List<Job> list = new ArrayList<>();

        for (int i = 0; i < jobsLength; i++) {
            list.add(new Job(i, jobs[i][0], jobs[i][1]));
        }

        list.sort((a, b) -> a.requestTime - b.requestTime);

        Queue<Job> jobQueue = new LinkedList<>(list);

        PriorityQueue<Job> controllerQueue = new PriorityQueue<>();

        Queue<Job> answerQueue = new LinkedList<>();

        Job runningJob = null;

        int time = 0;

        while (!(jobQueue.isEmpty() &&
                controllerQueue.isEmpty() &&
                runningJob == null)) {

            while (!jobQueue.isEmpty() &&
                    jobQueue.peek().requestTime <= time) {

                controllerQueue.offer(jobQueue.poll());
            }

            if (runningJob != null &&
                    time - runningJob.startTime == runningJob.workingTime) {

                runningJob.completedTime = time;
                answerQueue.offer(runningJob);

                runningJob = null;
            }

            if (runningJob == null &&
                    !controllerQueue.isEmpty()) {

                runningJob = controllerQueue.poll();
                runningJob.startTime = time;
            }

            time++;
        }

        int sum = 0;

        for (Job job : answerQueue) {
            sum += job.completedTime - job.requestTime;
        }

        return sum / jobsLength;
    }
}

class Job implements Comparable<Job> {
    int no;
    int requestTime;
    int workingTime;
    int startTime;
    int completedTime;

    public Job(int no, int requestTime, int workingTime) {
        this.no = no;
        this.requestTime = requestTime;
        this.workingTime = workingTime;
    }

    @Override
    public int compareTo(Job job) {
        if (this.workingTime != job.workingTime) {
            return this.workingTime - job.workingTime;
        }

        if (this.requestTime != job.requestTime) {
            return this.requestTime - job.requestTime;
        }

        return this.no - job.no;
    }
}