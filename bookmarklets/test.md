<style>
  .button {
      font: bold 16px Arial;
      text-decoration: none;
      background-color: #EEEEEE;
      color: #333333;
      padding: 2px 6px 2px 6px;
      border-top: 1px solid #CCCCCC;
      border-right: 1px solid #333333;
      border-bottom: 1px solid #333333;
      border-left: 1px solid #CCCCCC;
  }
</style>
<script>
  function allowDrop(ev) {
    ev.preventDefault();
  }

  function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
  }

  function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
  }
</script>

<h1>MOT Bookmarklets</h1>

<h2>What is a Bookmarklet?</h2>
<blockquote cite="https://en.wikipedia.org/wiki/Bookmarklet">
  "A bookmarklet is a bookmark stored in a web browser that contains JavaScript commands that add new features to the browser. They are stored as the URL of a bookmark in a web browser or as a hyperlink on a web page. Bookmarklets are usually small snippets of JavaScript executed when user clicks on them. When clicked, bookmarklets can perform a wide variety of operations, such as running a search query from selected text or extracting data from a table." - https://en.wikipedia.org/wiki/Bookmarklet
</blockquote>

<h2>The Bookmarklets!!</h2>

  <div id="div1" ondrop="drop(event)" ondragover="allowDrop(event)">
    <a class="button" draggable="true" ondragstart="drag(event)" href="javascript:(function()%7Bvar%20DOMAIN%3Dprompt(%22Enter%20DOMAIN-%20no%20www%3A%20%22)%2CWHO%3D%22https%3A%2F%2Fwhoisology.com%2F%22%2BDOMAIN%2CBW%3D%22https%3A%2F%2Fbuiltwith.com%2F%22%2BDOMAIN%2CDNSL%3D%22https%3A%2F%2Fdnslytics.com%2Fdomain%2F%22%2BDOMAIN%2CHOST%3D%22https%3A%2F%2Fhost.io%2F%22%2BDOMAIN%2CDT%3D%22https%3A%2F%2Fwhois.domaintools.com%2F%22%2BDOMAIN%2CVDNS%3D%22https%3A%2F%2Fviewdns.info%2Fwhois%2F%3Fdomain%3D%22%2BDOMAIN%2CREVIP%3D%22https%3A%2F%2Fviewdns.info%2Freverseip%2F%3Fhost%3D%22%2BDOMAIN%2B%22%26t%3D1%22%2CIPHIS%3D%22https%3A%2F%2Fviewdns.info%2Fiphistory%2F%3Fdomain%3D%22%2BDOMAIN%3Bwindow.open(DBD%2C%22_blank%22)%2Cwindow.open(WHO%2C%22_blank%22)%2Cwindow.open(BW%2C%22_blank%22)%2Cwindow.open(SPY%2C%22_blank%22)%2Cwindow.open(DNSL%2C%22_blank%22)%2Cwindow.open(HOST%2C%22_blank%22)%2Cwindow.open(DT%2C%22_blank%22)%2Cwindow.open(VDNS%2C%22_blank%22)%2Cwindow.open(REVIP%2C%22_blank%22)%2Cwindow.open(IPHIS%2C%22_blank%22)%7D)()">Domain Bookmarklet</a>
  </div>


<h2>What do I do with these files?</h2>
<h3>Easy Method</h3>
<ol>
  <li>Find the bookmarklet you want</li>
  <li>Click and drag it into your bookmarks bar.</li>
  <li>Click that bookmark to use the tool</li>
</ol>

<h3>More Manual Method</h3>
<ol>
  <li>Open the bookmarklet you wish to use.</li>
  <li>Scroll down to the <code>// Copy and paste the data below</code> section.</li>
  <li>Copy the text starting with <code>javascript:</code> and ending with <code>()</code></li>
  <li>Go to your favorite browser and make a new bookmark. We like doing this in our Bookmarks Bar but you can do it wherever.</li>
  <li>Name it whatever you wish.</li>
  <li>In the <code>URL</code> section, paste the code your copied. You need to paste everything from the <code>javascript:</code> all the way to the ending <code>()</code>.</li>
  <li>Save the bookmark/bookmarklet.</li>
  <li>Now you are set to run or use the bookmarklet. Some you need to be on a certain web page to use (like the Facebook ID one needs to be on a Facebook page like <code>https://www.facebook.com/zuck</code>). Navigate to the correct page or, for those that do not need a certain page, just click the bookmark.</li>
  <li><strong>WARNING:</strong> Some of these bookmarklets open one or more browser tabs. You may need to <strong>ALLOW POP-UPS</strong> in your web browser to get those tabs to show.</li>
</ol>

<hr>

<i>These tools are provided by the instructors and authors at <a target="_blank" href="https://www.myosint.training">My OSINT Training</a>. Check out our huge number of OSINT courses including our <strong>FREE</strong> <a target="_blank" href="https://www.myosint.training/courses/introduction-to-osint">Introduction to OSINT</a> course and our <a target="_blank" href="https://www.myosint.training/pages/bundles">bundles of classes.</a></i>
