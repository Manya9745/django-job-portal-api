from jobs.models import Job


def get_all_jobs():
    return Job.objects.all()


def create_job(validated_data):
    return Job.objects.create(**validated_data)