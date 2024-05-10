from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
Base = declarative_base()


class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    job = Column(String)
    team_leader = Column(String)
    work_size = Column(Integer)
    collaborators = Column(String)
    is_finished = Column(Boolean)


engine = create_engine('sqlite:///mars_explorer.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


@app.route('/')
def job_form():
    return render_template('task1.html')


@app.route('/add_job', methods=['POST'])
def add_job():
    session = Session()
    if request.method == 'POST':
        job = request.form['job']
        team_leader = request.form['team_leader']
        work_size = request.form['work_size']
        collaborators = request.form['collaborators']
        is_finished = 'is_finished' in request.form

        new_job = Job(job=job, team_leader=team_leader, work_size=work_size,
                      collaborators=collaborators, is_finished=is_finished)

        session.add(new_job)
        session.commit()
        session.close()

        return redirect(url_for('job_added'))
    else:
        return redirect(url_for('job_form'))


@app.route('/job_added')
def job_added():
    return "Job added successfully!"


if __name__ == '__main__':
    app.run(debug=True)
