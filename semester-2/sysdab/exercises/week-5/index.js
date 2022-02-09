const elements = [
    {
        title: 'html',
        description: 'Represents the root of an HTML document. Is always at the root of the document.'
    }, {
        title: 'head',
        description: 'Represents a collection of metadata for the document. If present it is the first element of the &lt;html&gt; element.'
    }, {
        title: 'title',
        description: 'Represents the documents title or name. Should be used to identify documents, if present it is inside the &lt;head&gt; element.'
    }, {
        title: 'body',
        description: 'Represents the content of the document. If present it is the second element of the &lt;html&gt; element.'
    }, {
        title: 'h1',
        description: 'Represents heading for the first section in the hierachy. The &lt;h1&gt; element has the highest rank while the &lt;h6&gt; has the lowest. Therefore this element has the highest rank.'
    }, {
        title: 'h2',
        description: 'Represents heading for the second section in the hierachy. The &lt;h1&gt; element has the highest rank while the &lt;h6&gt; has the lowest. Therefore this element has the second highest rank.'
    }, {
        title: 'p',
        description: 'Represents a paragraph. Should only be used when more specific elements are not applicable.'
    }, {
        title: 'nav',
        description: 'Represents a section of a page that links to other pages, or parts within the same page.'
    }, {
        title: 'ul',
        description: 'Represents list of unordered items. Contains &lt;li&gt; elements.'
    }, {
        title: 'li',
        description: 'Represents a list item. Should be inside a &lt;ol&gt; or &lt;ul&gt; element.'
    }, {
        title: 'a',
        description: 'Represents a link, if it has the "href" attribute. If not then it represents a placeholder where a link might be placed.'
    }, {
        title: 'main',
        description: 'Represents the main content of the &lt;body&gt; of a document.'
    }, {
        title: 'section',
        description: 'Represents a generic section of a document where a more specific element is not applicable. Should contain a header element to explain its purpose.'
    }, {
        title: 'footer',
        description: 'Represents the footer of a the nearest &lt;main&gt; element. Used as a footer, but also as appendices, indexes, license agreements etc.'
    }
]

let parent = document.getElementById('card-container');
elements.forEach(element => {
    let el = document.createElement('section');
    el.classList.add('card');

    el.innerHTML = `
        <div class="card-top">
            <p>
                &lt;${element.title} /&gt;
            </p>
        </div>
        <div class="card-body">
            <h4 class="card-title">
                The "${element.title}" tag
            </h4>
            <div class="card-content">
                <p>${element.description}</p>
            </div>
        </div>
    `

    parent.appendChild(el);
});


