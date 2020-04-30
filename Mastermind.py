from flask import Flask, escape, request, Response, render_template
from time import gmtime, strftime
from jinja2 import Template
app = Flask(__name__)
app.url_map.strict_slashes = False

html = """
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css ">
<style>
 h1 {
font-size: 120px !important;
  color: navy !important;

 }

option.rood{
    color:red
}
option.blauw{
    color:blue
}
option.groen{
    color:green
}
option.oranje{
    color:orange
}
option.paars{
    color:purple
}
option.geel{
    color:#eed000
}

h3.rood{
    color:red
}
h3.blauw{
    color:blue
}
h3.groen{
    color:green
}
h3.oranje{
    color:orange
}
h3.paars{
    color:purple
}
h3.geel{
    color:#eed000
}

select{
    font-size:50px
}

option{
    font-size:50pt

}

</style>

    </head>

    <body>

        <div class="container">
            <div class="row">
                <div class="col-sm">
                    <h1 > Mastermind </h1>
                    <p> Kraak de code! Je kan zo vaak proberen als je wilt! </p>
                </div>
            </div>
        </div>
        <div class="container">
            <div class="row">
                <div class="col-sm">
                    <h2> Aantal op de juiste plek: {{ juist }} </h2>
                    <h2> Aantal juist maar op de foute plek: {{ fout }} </h2>
                </div>
            </div>
        </div>
        <div class="container">
            <div class="row">
                <div class="col-sm">
                    <h3 {% if kleur0 == "Rood": %} class="rood" {% endif %}     {% if kleur0 == "Blauw": %} class="blauw" {% endif %}    {% if kleur0 == "Groen": %} class="groen" {% endif %}    {% if kleur0 == "Oranje": %} class="oranje" {% endif %}   {% if kleur0 == "Paars": %} class="paars" {% endif %}    {% if kleur0 == "Geel": %} class="geel" {% endif %}     > {{ kleur0 }} </h3>
                </div>
                <div class="col-sm">
                    <h3 {% if kleur1 == "Rood": %} class="rood" {% endif %}     {% if kleur1 == "Blauw": %} class="blauw" {% endif %}    {% if kleur1 == "Groen": %} class="groen" {% endif %}    {% if kleur1 == "Oranje": %} class="oranje" {% endif %}   {% if kleur1 == "Paars": %} class="paars" {% endif %}    {% if kleur1 == "Geel": %} class="geel" {% endif %}     > {{ kleur1 }} </h3>
                </div>
                <div class="col-sm">
                    <h3 {% if kleur2 == "Rood": %} class="rood" {% endif %}     {% if kleur2 == "Blauw": %} class="blauw" {% endif %}    {% if kleur2 == "Groen": %} class="groen" {% endif %}    {% if kleur2 == "Oranje": %} class="oranje" {% endif %}   {% if kleur2 == "Paars": %} class="paars" {% endif %}    {% if kleur2 == "Geel": %} class="geel" {% endif %}     > {{ kleur2 }} </h3>
                </div>
                <div class="col-sm">
                    <h3 {% if kleur3 == "Rood": %} class="rood" {% endif %}     {% if kleur3 == "Blauw": %} class="blauw" {% endif %}    {% if kleur3 == "Groen": %} class="groen" {% endif %}    {% if kleur3 == "Oranje": %} class="oranje" {% endif %}   {% if kleur3 == "Paars": %} class="paars" {% endif %}    {% if kleur3 == "Geel": %} class="geel" {% endif %}     > {{ kleur3 }} </h3>
                </div>
            </div>
        </div>







        <div class="container">
            <div class="row">
                <div class="col-sm">
                    <select class="custom-select"name="kleur0" form="mastermind">
                        <option class="rood" value="Rood"       {% if kleur0 == "Rood": %} selected {% endif %}     >      • Rood</option>
                        <option class="blauw" value="Blauw"     {% if kleur0 == "Blauw": %} selected {% endif %}    >    • Blauw</option>
                        <option class="groen" value="Groen"     {% if kleur0 == "Groen": %} selected {% endif %}    >    • Groen</option>
                        <option class="oranje" value="Oranje"   {% if kleur0 == "Oranje": %} selected {% endif %}   > • Oranje</option>
                        <option class="paars" value="Paars"     {% if kleur0 == "Paars": %} selected {% endif %}    >    • Paars</option>
                        <option class="geel" value="Geel"       {% if kleur0 == "Geel": %} selected {% endif %}     >       • Geel</option>
                    </select>
                </div>
                <div class="col-sm">
                    <select class="custom-select"name="kleur1" form="mastermind">
                        <option class="rood" value="Rood" {% if kleur1 == "Rood": %} selected {% endif %}>      • Rood</option>
                        <option class="blauw" value="Blauw"{% if kleur1 == "Blauw": %} selected {% endif %}>    • Blauw</option>
                        <option class="groen" value="Groen"{% if kleur1 == "Groen": %} selected {% endif %}>    • Groen</option>
                        <option class="oranje" value="Oranje"{% if kleur1 == "Oranje": %} selected {% endif %}> • Oranje</option>
                        <option class="paars" value="Paars"{% if kleur1 == "Paars": %} selected {% endif %}>    • Paars</option>
                        <option class="geel" value="Geel"{% if kleur1 == "Geel": %} selected {% endif %}>       • Geel</option>
                    </select>
                </div>
                <div class="col-sm">
                    <select class="custom-select"name="kleur2" form="mastermind">
                        <option class="rood" value="Rood" {% if kleur2 == "Rood": %} selected {% endif %}>      • Rood</option>
                        <option class="blauw" value="Blauw"{% if kleur2 == "Blauw": %} selected {% endif %}>    • Blauw</option>
                        <option class="groen" value="Groen"{% if kleur2 == "Groen": %} selected {% endif %}>    • Groen</option>
                        <option class="oranje" value="Oranje"{% if kleur2 == "Oranje": %} selected {% endif %}> • Oranje</option>
                        <option class="paars" value="Paars"{% if kleur2 == "Paars": %} selected {% endif %}>    • Paars</option>
                        <option class="geel" value="Geel"{% if kleur2 == "Geel": %} selected {% endif %}>       • Geel</option>
                    </select>
                </div>
                <div class="col-sm">
                    <select class="custom-select"name="kleur3" form="mastermind">
                        <option class="rood" value="Rood" {% if kleur3 == "Rood": %} selected {% endif %}>      • Rood</option>
                        <option class="blauw" value="Blauw"{% if kleur3 == "Blauw": %} selected {% endif %}>    • Blauw</option>
                        <option class="groen" value="Groen"{% if kleur3 == "Groen": %} selected {% endif %}>    • Groen</option>
                        <option class="oranje" value="Oranje"{% if kleur3 == "Oranje": %} selected {% endif %}> • Oranje</option>
                        <option class="paars" value="Paars"{% if kleur3 == "Paars": %} selected {% endif %}>    • Paars</option>
                        <option class="geel" value="Geel"{% if kleur3 == "Geel": %} selected {% endif %}>       • Geel</option>
                    </select>
                </div>
            </div>
        </div>
        <br \>
        <p \>
        <form action="/mastermind" id="mastermind">
            <div class="container">
                <div class="row">
                    <div class="col">
                        <input class="btn btn-info" type="submit" value="Controleer code">
                    </div>
                </div>
            </div>
        </form>
        <script>
        window.onload = function(){

            let list = document.getElementsByClassName("custom-select");

            for (var i = 0; i < list.length; i++) {
                let elem = list[i]
                elem.style.color = getComputedStyle(elem.options[elem.selectedIndex]).color;
                elem.onchange = function(){
                    elem.style.color = getComputedStyle(elem.options[elem.selectedIndex]).color;
                }
            }
        }

        </script>

    </body>
</html>
"""
@app.route('/favicon.ico')
def favicon():
    return "", 404

@app.route('/mastermind')
def mastermind():
    kleur0 = request.args.get('kleur0')
    kleur1 = request.args.get('kleur1')
    kleur2 = request.args.get('kleur2')
    kleur3 = request.args.get('kleur3')
    juist = 0
    fout = 0
    template = Template(html)
    if kleur0 == None or kleur1 == None or kleur2 == None or kleur3 == None:
        return template.render(kleur0="", kleur1="", kleur2="", kleur3="", juist=juist, fout=fout )

    inp = [kleur0, kleur1, kleur2, kleur3]
    code = ["Rood", "Groen", "Paars", "Oranje"]
   
    for i in range(len(code)):
        if inp[i] == code[i]:
            juist+=1

    for i in set(inp):
        if i in code:
            fout+=1

    fout -= juist
    


    return template.render(kleur0=kleur0, kleur1=kleur1, kleur2=kleur2, kleur3=kleur3, juist=juist, fout=fout )





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001)
