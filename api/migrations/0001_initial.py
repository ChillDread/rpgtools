# Generated by Django 3.1.1 on 2021-02-10 18:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionRunner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_input', models.TextField(verbose_name='Input')),
                ('additional_input', models.TextField(blank=True, null=True, verbose_name='Additional Input')),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DieRoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('die_size', models.PositiveIntegerField(default=0)),
                ('die_count', models.PositiveIntegerField(default=0)),
                ('per_modifier', models.TextField(blank=True, null=True)),
                ('roll_modifier', models.TextField(blank=True, null=True)),
                ('post_modifier', models.TextField(blank=True, null=True)),
                ('reroll', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BookFormat',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='_ID')),
                ('id', models.CharField(editable=False, max_length=256, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('read_me', models.TextField(blank=True, null=True, verbose_name='Read Me')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('format_type', models.CharField(choices=[('Physical', 'Physical'), ('Digital', 'Digital')], default='Physical', max_length=64, verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Book Format',
                'verbose_name_plural': 'Book Formats',
                'db_table': 'book_format',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='_ID')),
                ('id', models.CharField(editable=False, max_length=256, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('read_me', models.TextField(blank=True, null=True, verbose_name='Read Me')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website')),
            ],
            options={
                'verbose_name': 'Contributor',
                'verbose_name_plural': 'Contributors',
                'db_table': 'contributor',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='_ID')),
                ('id', models.CharField(editable=False, max_length=256, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('read_me', models.TextField(blank=True, null=True, verbose_name='Read Me')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('short_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Short Name')),
                ('abbreviation', models.CharField(blank=True, max_length=8, null=True, verbose_name='Abbreviation')),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
                'db_table': 'game',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='GameSystem',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='_ID')),
                ('id', models.CharField(editable=False, max_length=256, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('read_me', models.TextField(blank=True, null=True, verbose_name='Read Me')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('short_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Short Name')),
                ('abbreviation', models.CharField(blank=True, max_length=8, null=True, verbose_name='Abbreviation')),
            ],
            options={
                'verbose_name': 'Game System',
                'verbose_name_plural': 'Game Systems',
                'db_table': 'game_system',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='_ID')),
                ('id', models.CharField(editable=False, max_length=256, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('read_me', models.TextField(blank=True, null=True, verbose_name='Read Me')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('abbreviation', models.CharField(blank=True, max_length=8, null=True, verbose_name='Abbreviation')),
            ],
            options={
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publishers',
                'db_table': 'publisher',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('contributor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.contributor')),
                ('abbreviation', models.CharField(blank=True, max_length=8, null=True, verbose_name='Abbreviation')),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
                'db_table': 'organization',
                'ordering': ('name',),
            },
            bases=('api.contributor',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('contributor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.contributor')),
                ('name_prefix', models.CharField(blank=True, max_length=6, null=True, verbose_name='Prefix')),
                ('name_first', models.CharField(max_length=25, verbose_name='First Name')),
                ('name_middle', models.CharField(blank=True, max_length=50, null=True, verbose_name='Middle Name')),
                ('name_last', models.CharField(max_length=25, verbose_name='Last Name')),
                ('name_suffix', models.CharField(blank=True, max_length=50, null=True, verbose_name='Prefix')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
                'db_table': 'person',
                'ordering': ('name',),
            },
            bases=('api.contributor',),
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='_ID')),
                ('id', models.CharField(editable=False, max_length=256, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('read_me', models.TextField(blank=True, null=True, verbose_name='Read Me')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('workflow_method', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], default='Manual', max_length=15, verbose_name='Method')),
                ('definition', models.TextField(blank=True, null=True, verbose_name='Definition')),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
                ('deprecated', models.BooleanField(default=False, verbose_name='Deprecated')),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.game')),
            ],
            options={
                'verbose_name': 'Workflow',
                'verbose_name_plural': 'Workflows',
                'db_table': 'workflow',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='HistoricalWorkflow',
            fields=[
                ('_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='_ID')),
                ('id', models.CharField(editable=False, max_length=256, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('read_me', models.TextField(blank=True, null=True, verbose_name='Read Me')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('workflow_method', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], default='Manual', max_length=15, verbose_name='Method')),
                ('definition', models.TextField(blank=True, null=True, verbose_name='Definition')),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
                ('deprecated', models.BooleanField(default=False, verbose_name='Deprecated')),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('game', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api.game')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Workflow',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPublisher',
            fields=[
                ('_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='_ID')),
                ('id', models.CharField(editable=False, max_length=256, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('read_me', models.TextField(blank=True, null=True, verbose_name='Read Me')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('abbreviation', models.CharField(blank=True, max_length=8, null=True, verbose_name='Abbreviation')),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Publisher',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPerson',
            fields=[
                ('contributor_ptr', models.ForeignKey(auto_created=True, blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, related_name='+', to='api.contributor')),
                ('_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='_ID')),
                ('id', models.CharField(editable=False, max_length=256, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('read_me', models.TextField(blank=True, null=True, verbose_name='Read Me')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('name_prefix', models.CharField(blank=True, max_length=6, null=True, verbose_name='Prefix')),
                ('name_first', models.CharField(max_length=25, verbose_name='First Name')),
                ('name_middle', models.CharField(blank=True, max_length=50, null=True, verbose_name='Middle Name')),
                ('name_last', models.CharField(max_length=25, verbose_name='Last Name')),
                ('name_suffix', models.CharField(blank=True, max_length=50, null=True, verbose_name='Prefix')),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Person',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalOrganization',
            fields=[
                ('contributor_ptr', models.ForeignKey(auto_created=True, blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, related_name='+', to='api.contributor')),
                ('_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='_ID')),
                ('id', models.CharField(editable=False, max_length=256, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('read_me', models.TextField(blank=True, null=True, verbose_name='Read Me')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('abbreviation', models.CharField(blank=True, max_length=8, null=True, verbose_name='Abbreviation')),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Organization',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalGameSystem',
            fields=[
                ('_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='_ID')),
                ('id', models.CharField(editable=False, max_length=256, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('read_me', models.TextField(blank=True, null=True, verbose_name='Read Me')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('short_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Short Name')),
                ('abbreviation', models.CharField(blank=True, max_length=8, null=True, verbose_name='Abbreviation')),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('publisher', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api.publisher')),
            ],
            options={
                'verbose_name': 'historical Game System',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalGame',
            fields=[
                ('_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='_ID')),
                ('id', models.CharField(editable=False, max_length=256, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('read_me', models.TextField(blank=True, null=True, verbose_name='Read Me')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('short_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Short Name')),
                ('abbreviation', models.CharField(blank=True, max_length=8, null=True, verbose_name='Abbreviation')),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('game_system', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api.gamesystem')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('publisher', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api.publisher')),
            ],
            options={
                'verbose_name': 'historical Game',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalContributor',
            fields=[
                ('_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='_ID')),
                ('id', models.CharField(editable=False, max_length=256, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('read_me', models.TextField(blank=True, null=True, verbose_name='Read Me')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Contributor',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalBookFormat',
            fields=[
                ('_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='_ID')),
                ('id', models.CharField(editable=False, max_length=256, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('read_me', models.TextField(blank=True, null=True, verbose_name='Read Me')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('format_type', models.CharField(choices=[('Physical', 'Physical'), ('Digital', 'Digital')], default='Physical', max_length=64, verbose_name='Type')),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Book Format',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalBook',
            fields=[
                ('_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='_ID')),
                ('id', models.CharField(editable=False, max_length=256, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('read_me', models.TextField(blank=True, null=True, verbose_name='Read Me')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('short_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Short Name')),
                ('abbreviation', models.CharField(blank=True, max_length=8, null=True, verbose_name='Abbreviation')),
                ('catalog_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Catalog Number')),
                ('pages', models.IntegerField(blank=True, null=True, verbose_name='Pages')),
                ('publication_year', models.IntegerField(blank=True, null=True, verbose_name='Publication Year')),
                ('isbn_10', models.CharField(blank=True, max_length=18, null=True, validators=[django.core.validators.RegexValidator('^(?:ISBN(?:10)?(?:\\-10)?\\x20)?[0-9]{9}(\\d|X)$', 'Only ISNB-10 formatted strings are allowd.')], verbose_name='ISBN-10')),
                ('isbn_13', models.CharField(blank=True, max_length=21, null=True, validators=[django.core.validators.RegexValidator('^(?:ISBN(?:13)?(?:\\-13)?\\x20)?:?97(?:8|9)[0-9]{10}$', 'Only ISNB-13 formatted strings are allowd.')], verbose_name='ISBN-13')),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('book_format', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api.bookformat')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('publisher', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api.publisher', verbose_name='Publisher')),
            ],
            options={
                'verbose_name': 'historical Book',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='gamesystem',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.publisher'),
        ),
        migrations.AddField(
            model_name='game',
            name='game_system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.gamesystem'),
        ),
        migrations.AddField(
            model_name='game',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.publisher'),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='_ID')),
                ('id', models.CharField(editable=False, max_length=256, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('read_me', models.TextField(blank=True, null=True, verbose_name='Read Me')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('short_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Short Name')),
                ('abbreviation', models.CharField(blank=True, max_length=8, null=True, verbose_name='Abbreviation')),
                ('catalog_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Catalog Number')),
                ('pages', models.IntegerField(blank=True, null=True, verbose_name='Pages')),
                ('publication_year', models.IntegerField(blank=True, null=True, verbose_name='Publication Year')),
                ('isbn_10', models.CharField(blank=True, max_length=18, null=True, validators=[django.core.validators.RegexValidator('^(?:ISBN(?:10)?(?:\\-10)?\\x20)?[0-9]{9}(\\d|X)$', 'Only ISNB-10 formatted strings are allowd.')], verbose_name='ISBN-10')),
                ('isbn_13', models.CharField(blank=True, max_length=21, null=True, validators=[django.core.validators.RegexValidator('^(?:ISBN(?:13)?(?:\\-13)?\\x20)?:?97(?:8|9)[0-9]{10}$', 'Only ISNB-13 formatted strings are allowd.')], verbose_name='ISBN-13')),
                ('art_assistant', models.ManyToManyField(blank=True, related_name='art_assistant', to='api.Contributor', verbose_name='Art Assistant(s)')),
                ('art_director', models.ManyToManyField(blank=True, related_name='art_director', to='api.Contributor', verbose_name='Art Director(s)')),
                ('artist_cover', models.ManyToManyField(blank=True, related_name='artist_cover', to='api.Contributor', verbose_name='Cover Artist(s)')),
                ('artist_interior', models.ManyToManyField(blank=True, related_name='artist_interior', to='api.Contributor', verbose_name='Interior Artist(s)')),
                ('author', models.ManyToManyField(blank=True, related_name='author', to='api.Contributor', verbose_name='Author(s)')),
                ('book_format', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.bookformat')),
                ('designer', models.ManyToManyField(blank=True, related_name='designer', to='api.Contributor', verbose_name='Designer(s)')),
                ('developer', models.ManyToManyField(blank=True, related_name='developer', to='api.Contributor', verbose_name='Developer(s)')),
                ('editor', models.ManyToManyField(blank=True, related_name='editor', to='api.Contributor', verbose_name='Editor(s)')),
                ('game', models.ManyToManyField(blank=True, to='api.Game', verbose_name='Game(s)')),
                ('graphic_designer', models.ManyToManyField(blank=True, related_name='graphic_designer', to='api.Contributor', verbose_name='Graphic Designer(s)')),
                ('play_tester', models.ManyToManyField(blank=True, related_name='play_tester', to='api.Contributor', verbose_name='Play Tester(s)')),
                ('proofreader', models.ManyToManyField(blank=True, related_name='proofreader', to='api.Contributor', verbose_name='Proofreader(s)')),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.publisher', verbose_name='Publisher')),
                ('research_assistant', models.ManyToManyField(blank=True, related_name='research_assistant', to='api.Contributor', verbose_name='Research Assistant(s)')),
                ('text_manager', models.ManyToManyField(blank=True, related_name='text_manager', to='api.Contributor', verbose_name='Text Manager(s)')),
                ('text_processor', models.ManyToManyField(blank=True, related_name='text_processor', to='api.Contributor', verbose_name='Text Processor(s)')),
                ('type_setter', models.ManyToManyField(blank=True, related_name='type_setter', to='api.Contributor', verbose_name='Type Setter(s)')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'book',
                'ordering': ('name',),
            },
        ),
    ]
