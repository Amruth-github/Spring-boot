package com.example.demo;

import com.example.demo.model.Person;
import com.example.demo.repo.PersonRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.rest.webmvc.ResourceNotFoundException;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class PersonController {
    @Autowired
    PersonRepo repo;
    @PostMapping("/addPerson")
    public void addPerson(@RequestBody Person person) {
        repo.save(person);
    }

    @GetMapping("/getPeople")
    public List<Person> getPersonByName() {
        return repo.findAll();
    }
    @GetMapping("/getPersonbyId/{personid}")
    public Person getPersonById(@PathVariable long personid) {
        return repo.findById(personid).orElseThrow(() -> new ResourceNotFoundException(Integer.toString((int)personid)));
    }

    @DeleteMapping("/deleteById/{personid}")
    public void deletePerson(@PathVariable("personid") long personid) {
        repo.deleteById(personid);
    }

    @PutMapping("/update")
    public void updatePerson(@RequestBody Person person) {
        repo.save(person);
    }
}
