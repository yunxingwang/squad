from django.db import models


class Group(models.Model):
    slug = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, null=True)


class Project(models.Model):
    group = models.ForeignKey(Group, related_name='projects')
    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)

    class Meta:
        unique_together = ('group', 'slug',)


class Build(models.Model):
    project = models.ForeignKey(Project, related_name='builds')
    version = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('project', 'version',)


class Environment(models.Model):
    project = models.ForeignKey(Project, related_name='environments')
    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)

    class Meta:
        unique_together = ('project', 'slug',)


class TestRun(models.Model):
    build = models.ForeignKey(Build, related_name='test_runs')
    environment = models.ForeignKey(Environment, related_name='test_runs')
    created_at = models.DateTimeField(auto_now_add=True)


class Suite(models.Model):
    project = models.ForeignKey(Project, related_name='suites')
    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)

    class Meta:
        unique_together = ('project', 'slug',)


class Test(models.Model):
    test_run = models.ForeignKey(TestRun, related_name='tests')
    suite = models.ForeignKey(Suite)
    result = models.BooleanField()


class Benchmark(models.Model):
    test_run = models.ForeignKey(TestRun, related_name='benchmarks')
    suite = models.ForeignKey(Suite)
    result = models.FloatField()
    measurements = models.TextField()  # comma-separated float numbers

    @property
    def measurement_list(self):
        [float(n) for n in self.measurements.split(',')]