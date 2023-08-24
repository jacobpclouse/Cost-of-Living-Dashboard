@app.route('/report', methods=['POST', 'GET'])
def reportAnIssue():
    title = "JPC Bug Tracker | Report an Issue"

    if request.method == "POST":

        # 1st Step -- Adding to DB
        # need to have them all part of an object then add the object
        issue_Reporter = request.form["html_reporter"]
        ##add_reporter = Issues(issueReporter=issue_Reporter)

        reporter_Phone = request.form["html_phone"]
        ##add_phone = Issues(reporterPhone=reporter_Phone)

        issue_Title = request.form["html_title"]
        ##add_title = Issues(issueTitle=issue_Title)

        issue_Description = request.form["html_description"]
        ##add_description = Issues(issueDescription=issue_Description)

        issue_Location = request.form["html_location"]
        ##add_location = Issues(issueLocation=issue_Location)

        issue_Type = request.form["html_archetype"]
        ##add_type = Issues(issueType=issue_Type)

        # Putting all values into one object and then adding/commiting that to the DB
        addAllVal = Issues(issueReporter=issue_Reporter,reporterPhone=reporter_Phone,issueTitle=issue_Title,issueDescription=issue_Description,issueLocation=issue_Location,issueType=issue_Type)
## ASENDING ORDER BELOW
        try:
            #db.session.add(add_reporter,add_phone,add_title,add_description,add_location,add_type)
            ##db.session.add(add_reporter)
            db.session.add(addAllVal)
            db.session.commit()
            return redirect('/unhandled')

        except: 
            return redirect('/404', title = title) # if there is an issue, will return to 404 page
    else:
        return render_template('report_an_issue.html', title = title)
