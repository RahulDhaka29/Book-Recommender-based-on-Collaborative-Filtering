from flask import Flask, render_template,request
import pickle
import numpy as np

popular_df=pickle.load(open('popular.pkl','rb'))
pt=pickle.load(open('pt.pkl','rb'))
books=pickle.load(open('books.pkl','rb'))
similarity_scores=pickle.load(open('similarity_scores.pkl','rb'))


app=Flask(__name__)

@app.route('/')
def index():
    """
    Renders the home page with the top 50 most popular books.
    """
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=[round(r, 2) for r in popular_df['avg_rating'].values]
                           )


@app.route('/recommend')
def recommend_ui():
    """
    Renders the recommendation page UI.
    Passes a list of all book titles for potential autocomplete in the future.
    """
    return render_template('recommend.html', book_list=list(pt.index))

@app.route('/recommend_books', methods=['post'])
def recommend():
    """
    Handles the book recommendation logic based on user input.
    Includes error handling for when a book is not found.
    """
    user_input=request.form.get('user_input')
    # --- FIX 2: Error Handling ---
    # Find the index of the book entered by the user
    indices = np.where(pt.index == user_input)[0]

    if len(indices) == 0:
        # If the book is not found, return an error message to the template
        error_message = f"Sorry, the book '{user_input}' was not found in our database. Please check the spelling or try another title from the list."
        return render_template('recommend.html', error_message=error_message, book_list=list(pt.index))

    # If the book is found, proceed with recommendation
    index = indices[0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)

    return render_template('recommend.html', data=data, book_list=list(pt.index))


@app.route('/about')
def about():
    """ Renders the about page. """
    return render_template('about.html')

@app.route('/contact')
def contact():
    """ Renders the contact page. """
    return render_template('contact.html')


    
    # index=np.where(pt.index==user_input)[0][0]
    # # distances=similarity_scores[index]
    # similar_items=sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:6]
    
    # data=[]
    # for i in similar_items:
    #     # print(pt.index[i[0]])
    #     item=[]
    #     temp_df=books[books['Book-Title']==pt.index[i[0]]]
    #     item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
    #     item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
    #     item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
    #     data.append(item)
        
        
    # print(data)
    # return render_template('recommend.html', data=data)
if __name__=='__main__':
    app.run(debug=True)
    
    